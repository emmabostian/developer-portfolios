#!/usr/bin/env python3
"""Detect portfolio links whose domains redirect to ad/parking pages.

Strategy (two-phase to minimise network cost):
  1. HEAD request to every URL — cheap, follows redirects, captures final URL.
  2. Only when the final domain differs from the original do we issue a GET
     request and inspect the page body for parking keywords.

This means the ~95% of links that stay on their own domain cost only one fast
HEAD request each. Expensive GET+content checks are reserved for the small
subset that actually redirected somewhere unexpected.

Usage:
  python src/check_parking_redirects.py                    # dry-run, prints report
  python src/check_parking_redirects.py --output out.md    # write markdown report
  python src/check_parking_redirects.py --lychee-out ./lychee/out.md  # append to lychee output
  python src/check_parking_redirects.py --concurrency 20  # parallel workers (default: 20)
  python src/check_parking_redirects.py --timeout 10      # per-request timeout (default: 10)
"""
import argparse
import re
import ssl
import sys
import urllib.request
import urllib.error
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import urlparse

# ---------------------------------------------------------------------------
# Detection tables
# ---------------------------------------------------------------------------

PARKING_DOMAINS = {
    "sedoparking.com", "sedo.com", "bodis.com", "parkingcrew.net",
    "sav.com", "dan.com", "afternic.com", "hugedomains.com",
    "undeveloped.com", "buydomains.com", "brandbucket.com", "efty.com",
    "domainmarket.com", "above.com", "parklogic.com", "uniregistry.com",
    "domainnameshop.com", "registrar-servers.com", "topdns.com",
    "godaddysites.com", "secureserver.net", "domaincontrol.com",
    "domainnamesales.com", "domainagents.com", "squadhelp.com",
    "flippa.com", "epik.com",
}

PARKING_PHRASES = [
    "domain for sale",
    "buy this domain",
    "this domain is for sale",
    "make an offer",
    "parked domain",
    "this domain is parked",
    "domain parking",
    "purchase this domain",
    "inquire about this domain",
    "this web page is parked",
    "the domain has expired",
    "domain has expired",
    "this domain expired",
    "renew this domain",
    "domain registration expired",
]

_USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
)

_LINK_RE = re.compile(r"^-\s+\[([^\]]+)\]\(([^)]+)\)")

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _ssl_ctx():
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    return ctx


def _netloc(url: str) -> str:
    try:
        n = urlparse(url).netloc.lower()
        return n[4:] if n.startswith("www.") else n
    except Exception:
        return ""


def _is_parking_domain(url: str) -> bool:
    domain = _netloc(url)
    return any(domain == p or domain.endswith("." + p) for p in PARKING_DOMAINS)


def _has_parking_content(text: str) -> tuple:
    """Return (True, matched_phrase) or (False, '')."""
    lower = text.lower()
    for phrase in PARKING_PHRASES:
        if phrase in lower:
            return True, phrase
    return False, ""


def _make_request(url: str, method: str, timeout: int) -> urllib.request.Request:
    req = urllib.request.Request(url, method=method)
    req.add_header("User-Agent", _USER_AGENT)
    req.add_header("Accept", "text/html,application/xhtml+xml,*/*;q=0.8")
    return req


def _follow(url: str, method: str, timeout: int):
    """Open url, return (response, final_url). Raises on error."""
    req = _make_request(url, method, timeout)
    resp = urllib.request.urlopen(req, timeout=timeout, context=_ssl_ctx())
    return resp, resp.url


# ---------------------------------------------------------------------------
# Per-URL check
# ---------------------------------------------------------------------------

def check_url(url: str, timeout: int) -> dict:
    result = {"url": url, "final_url": url, "status": "ok", "reason": ""}

    # --- Phase 1: HEAD (fast, no body) ---
    try:
        resp, final_url = _follow(url, "HEAD", timeout)
        result["final_url"] = final_url

        if _is_parking_domain(final_url):
            result["status"] = "ad"
            result["reason"] = f"HEAD redirects to parking domain: {_netloc(final_url)}"
            return result

        orig_domain = _netloc(url)
        final_domain = _netloc(final_url)
        domain_changed = orig_domain and final_domain and orig_domain != final_domain

        # If domain stayed the same and isn't a known parking domain, we're done
        if not domain_changed:
            return result

    except urllib.error.HTTPError as e:
        if e.code in (404, 410):
            result["status"] = "dead"
            result["reason"] = f"HTTP {e.code}"
            return result
        # HEAD rejected — fall through to GET phase
        final_url = url
        domain_changed = False
    except urllib.error.URLError as e:
        reason = str(e.reason).lower() if hasattr(e, "reason") else str(e).lower()
        if any(k in reason for k in ("name or service not known", "nodename nor servname",
                                      "failed to resolve", "no address associated")):
            result["status"] = "dead"
            result["reason"] = "DNS resolution failed — domain likely expired"
        else:
            result["status"] = "timeout" if "timed out" in reason else "error"
            result["reason"] = str(e.reason) if hasattr(e, "reason") else str(e)
        return result
    except Exception as e:
        result["status"] = "error"
        result["reason"] = str(e)
        return result

    # --- Phase 2: GET + content check (only for cross-domain redirects) ---
    try:
        resp, final_url = _follow(url, "GET", timeout)
        result["final_url"] = final_url

        if _is_parking_domain(final_url):
            result["status"] = "ad"
            result["reason"] = f"GET redirects to parking domain: {_netloc(final_url)}"
            return result

        body = resp.read(65_536).decode("utf-8", errors="replace")
        matched, phrase = _has_parking_content(body)
        if matched:
            result["status"] = "ad"
            result["reason"] = f"page contains parking keyword: \"{phrase}\""
            return result

    except Exception:
        # Phase 2 failure is non-fatal — phase 1 passed, treat as ok
        pass

    return result


# ---------------------------------------------------------------------------
# README parsing
# ---------------------------------------------------------------------------

def extract_links(lines):
    """Return [(line_idx, name, url), ...]."""
    out = []
    for i, line in enumerate(lines):
        m = _LINK_RE.match(line.strip())
        if m:
            out.append((i, m.group(1), m.group(2)))
    return out


def parse_lychee_flagged_urls(lychee_path: str) -> set:
    """Extract URLs already flagged by lychee so we can skip them."""
    try:
        with open(lychee_path, "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        return set()
    # lychee out.md lines look like:  | https://... | ... | ... |
    # or plain lines:  - [Error] https://...
    url_re = re.compile(r"https?://[^\s|>\"')\]]+")
    return set(url_re.findall(content))


# ---------------------------------------------------------------------------
# Main scan
# ---------------------------------------------------------------------------

def scan(lines, concurrency: int, timeout: int, skip_urls: set, verbose: bool):
    entries = extract_links(lines)
    checkable = [(i, n, u) for i, n, u in entries if u not in skip_urls]
    skipped = len(entries) - len(checkable)

    print(
        f"Checking {len(checkable)} links "
        f"({skipped} already flagged by lychee, skipped) …"
    )

    flagged = []
    with ThreadPoolExecutor(max_workers=concurrency) as pool:
        futures = {pool.submit(check_url, url, timeout): (idx, name, url)
                   for idx, name, url in checkable}
        done = 0
        total = len(futures)
        for future in as_completed(futures):
            done += 1
            idx, name, url = futures[future]
            try:
                result = future.result()
            except Exception as e:
                result = {"url": url, "final_url": url, "status": "error", "reason": str(e)}
            result["line_idx"] = idx
            result["name"] = name

            if result["status"] in ("ad", "dead"):
                flagged.append(result)
                label = "AD/PARKED" if result["status"] == "ad" else "DEAD"
                print(f"  [{done}/{total}] [{label}] {name} — {result['reason']}")
            elif verbose:
                print(f"  [{done}/{total}] ok  {name}")

    return flagged


# ---------------------------------------------------------------------------
# Report formatting
# ---------------------------------------------------------------------------

def build_markdown(flagged: list) -> str:
    if not flagged:
        return ""
    lines = [
        "",
        "## Ad/Parking Redirect Report",
        "",
        f"Found **{len(flagged)}** link(s) redirecting to ad or parking pages:",
        "",
        "| Line | Name | URL | Reason |",
        "| ---- | ---- | --- | ------ |",
    ]
    for r in sorted(flagged, key=lambda x: x["line_idx"]):
        name = r["name"].replace("|", "\\|")
        url = r["url"]
        reason = r["reason"].replace("|", "\\|")
        lines.append(f"| {r['line_idx'] + 1} | {name} | {url} | {reason} |")
    lines.append("")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main(argv=None):
    p = argparse.ArgumentParser(
        description="Detect portfolio links redirecting to ad/parking pages"
    )
    p.add_argument("--readme", default="README.md")
    p.add_argument("--lychee-out", default="", metavar="PATH",
                   help="Path to lychee out.md — its flagged URLs are skipped")
    p.add_argument("--output", default="", metavar="PATH",
                   help="Write markdown report to this file (appends if lychee-out is the same path)")
    p.add_argument("--concurrency", type=int, default=20)
    p.add_argument("--timeout", type=int, default=10)
    p.add_argument("--verbose", action="store_true")
    args = p.parse_args(argv)

    try:
        with open(args.readme, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"ERROR: {args.readme} not found", file=sys.stderr)
        return 2

    skip_urls = parse_lychee_flagged_urls(args.lychee_out) if args.lychee_out else set()
    flagged = scan(lines, args.concurrency, args.timeout, skip_urls, args.verbose)

    print()
    if not flagged:
        print("No ad/parking redirects detected.")
        return 0

    report = build_markdown(flagged)
    print(report)

    if args.output:
        mode = "a" if args.output == args.lychee_out else "w"
        with open(args.output, mode, encoding="utf-8") as f:
            f.write(report)
        action = "Appended to" if mode == "a" else "Wrote"
        print(f"{action} {args.output}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
