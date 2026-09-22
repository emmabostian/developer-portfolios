#!/usr/bin/env python3
"""Sorting and metadata helpers for the developer portfolio feed.

The README keeps portfolios in alphabetical order and feed.json is generated
from it.  That fixed ordering makes discovery hard as the list grows.  This
module adds the data plumbing and the sorting logic behind the UI sorting
control (Newest, Most Popular, Most Viewed/Clicked):

* :data:`SORT_OPTIONS` lists the supported sort modes.
* :func:`sort_portfolios` returns a new, sorted list (the input is never
  mutated) that is safe to serve straight to a web application.
* :func:`enrich_with_git_dates` fills ``date_added`` from the git history of
  README.md, which is the only in-repo source for "when was this portfolio
  added".
* :func:`load_metrics` loads optional ``views``/``clicks``/``popularity``
  numbers from ``portfolio_metrics.json``.
* :func:`preserve_metadata` keeps previously generated metadata when
  feed.json is regenerated.
* Running the module sorts a feed file from the command line::

      python src/portfolio_sorting.py --by newest --limit 20
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from datetime import date, datetime, timezone
from urllib.parse import urlsplit, urlunsplit

DEFAULT_FEED_PATH = "feed.json"
DEFAULT_METRICS_PATH = "portfolio_metrics.json"

#: Sort option id -> label shown in the UI.  Insertion order is the order the
#: options should be presented in.
SORT_OPTIONS = {
    "name": "Name (A-Z)",
    "newest": "Newest",
    "popular": "Most Popular",
    "views": "Most Viewed/Clicked",
}

#: Friendly aliases accepted from CLI flags / query strings.
SORT_ALIASES = {
    "alphabetical": "name",
    "a-z": "name",
    "az": "name",
    "recent": "newest",
    "most-recent": "newest",
    "most_recent": "newest",
    "new": "newest",
    "most-popular": "popular",
    "most_popular": "popular",
    "popularity": "popular",
    "most-viewed": "views",
    "most_viewed": "views",
    "most-clicked": "views",
    "most_clicked": "views",
    "viewed": "views",
    "clicked": "views",
}

#: Metadata fields that may be attached to a feed entry.  They are optional
#: for backward compatibility: consumers that do not know about them keep
#: working unchanged.
METADATA_FIELDS = ("date_added", "views", "clicks", "popularity")

#: Canonical field order for generated feed entries.
FIELD_ORDER = ("name", "url", "tagline", "date_added", "views", "clicks", "popularity")

_ENTRY_LINE_RE = re.compile(r"^\+\s*-\s+\[([^\]]+)\]\(([^)]+)\)")
_ISO_PREFIX_RE = re.compile(r"^(\d{4})-(\d{2})-(\d{2})")


def normalize_sort_option(value):
    """Return the canonical sort option id for *value*.

    Raises :class:`ValueError` for unknown options so typos fail loudly
    instead of silently falling back to alphabetical order.
    """
    key = str(value or "").strip().lower()
    key = SORT_ALIASES.get(key, key)
    if key not in SORT_OPTIONS:
        raise ValueError(
            "Unknown sort option: {!r}. Valid options: {}".format(
                value, ", ".join(SORT_OPTIONS)
            )
        )
    return key


def sort_label(value):
    """Return the human-readable label for a sort option."""
    return SORT_OPTIONS[normalize_sort_option(value)]


def normalize_url(url):
    """Normalize a portfolio URL for lookups.

    Lowercases the scheme/host, drops the fragment and ignores a trailing
    slash so that ``https://Example.com/`` and ``https://example.com`` refer
    to the same portfolio when metadata is merged.
    """
    text = str(url or "").strip()
    if not text:
        return ""
    parts = urlsplit(text)
    path = parts.path
    if path.endswith("/"):
        path = path[:-1]
    return urlunsplit((parts.scheme.lower(), parts.netloc.lower(), path, parts.query, ""))


def to_number(value, default=0.0):
    """Best-effort conversion of *value* to a number.

    ``bool`` is rejected on purpose (``True`` is not a view count) and
    anything that cannot be parsed falls back to *default*.
    """
    if isinstance(value, bool) or value is None:
        return default
    if isinstance(value, (int, float)):
        return value
    if isinstance(value, str):
        try:
            return float(value.strip())
        except (TypeError, ValueError):
            return default
    return default


def parse_added_date(value):
    """Parse a ``date_added`` value into :class:`datetime.date` or ``None``.

    Accepts ISO dates (``2024-03-15``), ISO timestamps and Unix epoch
    timestamps (seconds).
    """
    if isinstance(value, bool) or value is None:
        return None
    if isinstance(value, (int, float)):
        try:
            return datetime.fromtimestamp(value, tz=timezone.utc).date()
        except (OverflowError, OSError, ValueError):
            return None
    if not isinstance(value, str):
        return None
    text = value.strip()
    if not text:
        return None
    match = _ISO_PREFIX_RE.match(text)
    if match:
        try:
            return date(int(match.group(1)), int(match.group(2)), int(match.group(3)))
        except ValueError:
            return None
    try:
        return datetime.fromisoformat(text.replace("Z", "+00:00")).date()
    except ValueError:
        return None


def popularity_score(entry):
    """Return the popularity metric for *entry*.

    An explicit ``popularity`` value always wins (curators can pin entries or
    feed a weighted score in).  Otherwise popularity is the total engagement:
    ``views + clicks``.
    """
    if entry.get("popularity") is not None:
        return to_number(entry.get("popularity"))
    return to_number(entry.get("views")) + to_number(entry.get("clicks"))


def _name_key(entry):
    name = str(entry.get("name") or "")
    return (name.casefold(), name)


def _newest_key(entry):
    added = parse_added_date(entry.get("date_added"))
    if added is None:
        # Entries without a known date sort last, alphabetically among
        # themselves.
        return (1, 0, _name_key(entry))
    # Negated ordinal gives newest-first while staying sortable in ascending
    # order (so ties fall back to the name key deterministically).
    return (0, -added.toordinal(), _name_key(entry))


def _popular_key(entry):
    return (-popularity_score(entry), _name_key(entry))


def _views_key(entry):
    return (-to_number(entry.get("views")), -to_number(entry.get("clicks")), _name_key(entry))


_SORT_KEYS = {
    "name": _name_key,
    "newest": _newest_key,
    "popular": _popular_key,
    "views": _views_key,
}


def sort_portfolios(portfolios, sort_by="name"):
    """Return a new list of *portfolios* ordered by *sort_by*.

    Supported options (see :data:`SORT_OPTIONS`):

    ``name``
        Alphabetical by name (case-insensitive).  This is the historical
        ordering and the default.
    ``newest``
        Most recently added first, based on the ``date_added`` field.
    ``popular``
        Highest ``popularity`` score first (falls back to ``views + clicks``).
    ``views``
        Most viewed/clicked first: ``views``, then ``clicks``.

    The input list is never modified.  Entries missing a given metric are
    ordered after entries that have one, and alphabetical order is used to
    break ties so results are stable and deterministic.
    """
    option = normalize_sort_option(sort_by)
    return sorted(portfolios, key=_SORT_KEYS[option])


def metadata_from_feed(portfolios):
    """Build a ``normalized url -> metadata`` mapping from feed entries."""
    metadata = {}
    for entry in portfolios or []:
        url = normalize_url(entry.get("url"))
        if not url:
            continue
        meta = {field: entry[field] for field in METADATA_FIELDS if entry.get(field) is not None}
        if meta:
            metadata.setdefault(url, meta)
    return metadata


def merge_metadata(portfolios, metadata, fields=METADATA_FIELDS):
    """Return copies of *portfolios* with metadata from *metadata* applied.

    *metadata* maps a normalized (or plain) URL to a dict of values.  Only
    keys listed in *fields* and present in the metadata are copied, so
    existing values survive when a metrics file is incomplete.
    """
    merged = []
    for entry in portfolios:
        new_entry = dict(entry)
        meta = metadata.get(normalize_url(entry.get("url")))
        if not meta and entry.get("url") in metadata:
            meta = metadata[entry.get("url")]
        if meta:
            for field in fields:
                value = meta.get(field)
                if value is not None:
                    new_entry[field] = value
        merged.append(new_entry)
    return merged


def preserve_metadata(portfolios, previous, fields=METADATA_FIELDS):
    """Carry metadata over from previously generated *previous* entries.

    Used so regenerating feed.json never drops fields that are expensive to
    recompute (like ``date_added``) or that come from an external analytics
    source.
    """
    return merge_metadata(portfolios, metadata_from_feed(previous), fields=fields)


def order_entry_fields(entry):
    """Return *entry* as a dict with the canonical feed field order."""
    ordered = {field: entry[field] for field in FIELD_ORDER if field in entry}
    for key, value in entry.items():
        if key not in ordered:
            ordered[key] = value
    return ordered


def parse_added_dates(git_log_output):
    """Parse ``git log -p`` output into earliest-add timestamp maps.

    Returns ``(by_url, by_name)`` where ``by_url`` maps normalized URLs and
    ``by_name`` maps case-folded names to Unix timestamps.  Removed entries
    are included: the earliest appearance in history is what we want.
    """
    by_url = {}
    by_name = {}
    timestamp = None
    for line in git_log_output.splitlines():
        if line.startswith("@@@"):
            try:
                timestamp = int(line[3:].strip())
            except ValueError:
                timestamp = None
            continue
        if timestamp is None:
            continue
        match = _ENTRY_LINE_RE.match(line)
        if not match:
            continue
        name = match.group(1).strip()
        url = normalize_url(match.group(2))
        if url and url not in by_url:
            by_url[url] = timestamp
        name_key = name.casefold()
        if name_key and name_key not in by_name:
            by_name[name_key] = timestamp
    return by_url, by_name


def is_shallow_repository(repo_path="."):
    """Return True when ``repo_path`` is a shallow clone.

    Shallow clones only contain recent history, so deriving "date added"
    from them would be wrong.
    """
    try:
        proc = subprocess.run(
            ["git", "-C", str(repo_path), "rev-parse", "--is-shallow-repository"],
            capture_output=True,
            text=True,
        )
    except OSError:
        return False
    return proc.returncode == 0 and proc.stdout.strip() == "true"


def get_added_dates(repo_path="."):
    """Return ``(by_url, by_name)`` earliest-add timestamps from git history.

    Returns two empty mappings when git is unavailable (or README.md has no
    history yet) so callers can degrade gracefully.
    """
    cmd = [
        "git",
        "-C",
        str(repo_path),
        "log",
        "--reverse",
        "--unified=0",
        "--format=@@@%ct",
        "-p",
        "--",
        "README.md",
    ]
    try:
        proc = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
        )
    except OSError:
        return {}, {}
    if proc.returncode != 0:
        return {}, {}
    return parse_added_dates(proc.stdout)


def enrich_with_git_dates(portfolios, repo_path=".", refresh=False):
    """Attach ``date_added`` (ISO date) to entries using git history.

    Existing ``date_added`` values are kept unless *refresh* is true.
    """
    by_url, by_name = get_added_dates(repo_path)
    if not by_url:
        return [dict(entry) for entry in portfolios]

    metadata = {}
    for entry in portfolios:
        if entry.get("date_added") and not refresh:
            continue
        url = normalize_url(entry.get("url"))
        timestamp = by_url.get(url)
        if timestamp is None:
            timestamp = by_name.get(str(entry.get("name") or "").casefold())
        if timestamp is not None:
            added = datetime.fromtimestamp(timestamp, tz=timezone.utc).strftime("%Y-%m-%d")
            metadata[url] = {"date_added": added}
    return merge_metadata(portfolios, metadata)


def _metrics_from_items(items):
    """Build a metrics mapping from a list of ``{url, ...}`` dicts."""
    metadata = {}
    for item in items:
        if not isinstance(item, dict):
            continue
        url = item.get("url") or item.get("portfolio_url")
        if not url:
            continue
        meta = {field: item[field] for field in METADATA_FIELDS if item.get(field) is not None}
        if meta:
            metadata[normalize_url(url)] = meta
    return metadata


def load_metrics(path=DEFAULT_METRICS_PATH):
    """Load a portfolio metrics file.

    Accepted shapes::

        {"https://example.com": {"views": 120, "clicks": 8}}

        [{"url": "https://example.com", "views": 120, "clicks": 8}]

    A missing file yields ``{}`` so feed generation stays optional.  A
    malformed file prints a warning and yields ``{}`` instead of failing the
    build.
    """
    try:
        with open(path, "r", encoding="utf-8") as handle:
            data = json.load(handle)
    except FileNotFoundError:
        return {}
    except (OSError, json.JSONDecodeError) as exc:
        print("Warning: could not read metrics file {}: {}".format(path, exc), file=sys.stderr)
        return {}

    if isinstance(data, dict):
        nested = data.get("portfolios")
        if isinstance(nested, list):
            return _metrics_from_items(nested)
        return {
            normalize_url(url): {
                field: meta[field] for field in METADATA_FIELDS if meta.get(field) is not None
            }
            for url, meta in data.items()
            if isinstance(meta, dict)
        }
    if isinstance(data, list):
        return _metrics_from_items(data)
    return {}


def format_entry(entry):
    """Format one feed entry as a README-style markdown line."""
    name = entry.get("name", "")
    url = entry.get("url", "")
    line = "- [{}]({})".format(name, url)
    tagline = entry.get("tagline")
    if tagline:
        line += " [{}]".format(tagline)
    return line


def build_parser():
    parser = argparse.ArgumentParser(
        description="Sort the portfolio feed (and optionally print it as markdown).",
    )
    parser.add_argument(
        "--by",
        default="name",
        help="sort option: {} (default: name)".format(", ".join(SORT_OPTIONS)),
    )
    parser.add_argument(
        "--feed",
        default=DEFAULT_FEED_PATH,
        help="path to feed.json (default: {})".format(DEFAULT_FEED_PATH),
    )
    parser.add_argument("--limit", type=int, default=0, help="only output the first N entries")
    parser.add_argument(
        "--json",
        action="store_true",
        help="print JSON instead of markdown lines",
    )
    parser.add_argument(
        "--list-options",
        action="store_true",
        help="print the available sort options and exit",
    )
    return parser


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.list_options:
        for option, label in SORT_OPTIONS.items():
            print("{}: {}".format(option, label))
        return 0

    try:
        option = normalize_sort_option(args.by)
    except ValueError as exc:
        parser.error(str(exc))

    try:
        with open(args.feed, "r", encoding="utf-8") as handle:
            portfolios = json.load(handle)
    except (OSError, json.JSONDecodeError) as exc:
        print("Error: could not read {}: {}".format(args.feed, exc), file=sys.stderr)
        return 1

    if not isinstance(portfolios, list):
        print("Error: {} should contain a JSON list of portfolios".format(args.feed), file=sys.stderr)
        return 1

    portfolios = sort_portfolios(portfolios, option)
    if args.limit and args.limit > 0:
        portfolios = portfolios[: args.limit]

    if args.json:
        json.dump(portfolios, sys.stdout, indent=2, ensure_ascii=False)
        sys.stdout.write("\n")
    else:
        for entry in portfolios:
            print(format_entry(entry))
    return 0


if __name__ == "__main__":
    sys.exit(main())
