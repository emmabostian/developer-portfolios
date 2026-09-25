#!/usr/bin/env python3
"""
Generate feed.json from README.md

This script extracts all portfolio entries from README.md and creates
a JSON file with structured data for each portfolio.

Besides ``name``, ``url`` and the optional ``tagline``, entries can carry
metadata used by the sorting options (Newest, Most Popular, Most
Viewed/Clicked):

* ``date_added`` - the date an entry first appeared in README.md, derived
  from git history (requires a full clone).
* ``views`` / ``clicks`` - analytics counters loaded from an optional
  ``portfolio_metrics.json`` file.
* ``popularity`` - an explicit score that overrides ``views + clicks``.

Usage:
    python src/generate_feed.py
    python src/generate_feed.py --with-git-dates
    python src/generate_feed.py --metrics analytics/portfolio_metrics.json
"""

import argparse
import json
import os
import re
import sys

try:  # imported as a package (e.g. `from src import generate_feed`)
    from .portfolio_sorting import (
        DEFAULT_METRICS_PATH,
        enrich_with_git_dates,
        is_shallow_repository,
        load_metrics,
        merge_metadata,
        order_entry_fields,
        preserve_metadata,
    )
except ImportError:  # executed directly (`python src/generate_feed.py`)
    from portfolio_sorting import (
        DEFAULT_METRICS_PATH,
        enrich_with_git_dates,
        is_shallow_repository,
        load_metrics,
        merge_metadata,
        order_entry_fields,
        preserve_metadata,
    )


def extract_portfolio_data(lines):
    """
    Extract portfolio data from README lines.
    Returns a list of dictionaries with name, url, and optional tagline.

    Format expected:
    - [Name](url)
    - [Name](url) [tagline]
    """
    portfolios = []
    # Regex to match markdown links with optional tagline
    # Pattern: - [name](url) optional[tagline]
    pattern = re.compile(r'^-\s+\[([^\]]+)\]\(([^)]+)\)(?:\s+\[([^\]]*)\])?')

    for line in lines:
        match = pattern.match(line.strip())
        if match:
            name = match.group(1).strip()
            url = match.group(2).strip()
            tagline = match.group(3).strip() if match.group(3) else None

            portfolio_entry = {
                "name": name,
                "url": url
            }

            if tagline:
                portfolio_entry["tagline"] = tagline

            portfolios.append(portfolio_entry)

    return portfolios


def _load_previous_feed(path):
    """Read an existing feed file, returning [] when it is missing/invalid."""
    try:
        with open(path, "r", encoding="utf-8") as handle:
            data = json.load(handle)
    except (OSError, json.JSONDecodeError):
        return []
    return data if isinstance(data, list) else []


def _should_use_git_dates(repo_path):
    """Auto-detect whether git history can provide reliable add dates."""
    if not os.path.exists(os.path.join(repo_path, ".git")):
        return False
    return not is_shallow_repository(repo_path)


def create_feed_json(
    readme_path="README.md",
    output_path="feed.json",
    metrics_path=None,
    with_git_dates=None,
    refresh_dates=False,
    preserve_existing=True,
    repo_path=".",
):
    """
    Read README.md and create/update feed.json with portfolio data.
    Returns the number of portfolios extracted.

    ``with_git_dates`` defaults to ``None`` (auto): dates are derived from
    git history when running inside a full clone.  ``metrics_path`` defaults
    to ``portfolio_metrics.json``; a missing file is not an error.
    """
    try:
        with open(readme_path, "r", encoding="utf-8") as handle:
            lines = handle.readlines()
    except FileNotFoundError:
        print(f"Error: {readme_path} not found.")
        return 0
    except OSError as exc:
        print(f"Error reading {readme_path}: {exc}")
        return 0

    try:
        portfolios = extract_portfolio_data(lines)

        previous = _load_previous_feed(output_path) if preserve_existing else []
        if previous:
            portfolios = preserve_metadata(portfolios, previous)

        if with_git_dates is None:
            with_git_dates = _should_use_git_dates(repo_path)
        needs_dates = refresh_dates or any(not entry.get("date_added") for entry in portfolios)
        if with_git_dates and needs_dates:
            portfolios = enrich_with_git_dates(portfolios, repo_path=repo_path, refresh=refresh_dates)

        metrics_path = metrics_path or DEFAULT_METRICS_PATH
        if os.path.exists(metrics_path):
            metrics = load_metrics(metrics_path)
            if metrics:
                portfolios = merge_metadata(portfolios, metrics)

        portfolios = [order_entry_fields(entry) for entry in portfolios]

        with open(output_path, "w", encoding="utf-8") as handle:
            json.dump(portfolios, handle, indent=2, ensure_ascii=False)

        return len(portfolios)
    except Exception as exc:  # keep the historical contract of returning 0 on failure
        print(f"Error creating {output_path}: {exc}")
        return 0


def build_parser():
    parser = argparse.ArgumentParser(description="Generate feed.json from README.md.")
    parser.add_argument("--readme", default="README.md", help="path to README.md")
    parser.add_argument("--output", default="feed.json", help="path to write feed.json")
    parser.add_argument(
        "--metrics",
        default=None,
        help=f"path to a portfolio metrics JSON file (default: {DEFAULT_METRICS_PATH} when present)",
    )
    parser.add_argument(
        "--with-git-dates",
        dest="with_git_dates",
        action="store_true",
        default=None,
        help="force deriving date_added from git history (default: auto-detect)",
    )
    parser.add_argument(
        "--no-git-dates",
        dest="with_git_dates",
        action="store_false",
        help="never read date_added from git history",
    )
    parser.add_argument(
        "--refresh-dates",
        action="store_true",
        help="recompute date_added for every entry instead of only filling gaps",
    )
    parser.add_argument(
        "--no-preserve-metadata",
        action="store_true",
        help="do not carry metadata over from an existing feed.json",
    )
    parser.add_argument(
        "--repo",
        default=".",
        help="repository root used for git history lookups (default: .)",
    )
    return parser


def _safe_print(message):
    """Print *message*, falling back to ASCII on consoles without UTF-8."""
    try:
        print(message)
    except UnicodeEncodeError:
        print(message.encode("ascii", "replace").decode("ascii"))


def main(argv=None):
    """Main entry point for the script."""
    args = build_parser().parse_args(argv)
    portfolio_count = create_feed_json(
        readme_path=args.readme,
        output_path=args.output,
        metrics_path=args.metrics,
        with_git_dates=args.with_git_dates,
        refresh_dates=args.refresh_dates,
        preserve_existing=not args.no_preserve_metadata,
        repo_path=args.repo,
    )
    if portfolio_count:
        _safe_print(f"✓ Successfully created {args.output} with {portfolio_count} portfolio entries.")
        return 0
    else:
        _safe_print(f"✗ Failed to create {args.output}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
