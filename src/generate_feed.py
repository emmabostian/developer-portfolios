#!/usr/bin/env python3
"""
Generate feed.json from README.md

This script extracts all portfolio entries from README.md and creates
a JSON file with structured data for each portfolio.

Usage:
    python src/generate_feed.py
"""

import re
import json
import sys


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


def create_feed_json(readme_path="README.md", output_path="feed.json"):
    """
    Read README.md and create/update feed.json with portfolio data.
    Returns the number of portfolios extracted.
    """
    try:
        with open(readme_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        portfolios = extract_portfolio_data(lines)

        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(portfolios, f, indent=2, ensure_ascii=False)

        return len(portfolios)
    except FileNotFoundError:
        print(f"Error: {readme_path} not found.")
        return 0
    except Exception as e:
        print(f"Error creating feed.json: {e}")
        return 0


def main():
    """Main entry point for the script."""
    portfolio_count = create_feed_json()
    if portfolio_count:
        print(f"✓ Successfully created feed.json with {portfolio_count} portfolio entries.")
        return 0
    else:
        print("✗ Failed to create feed.json")
        return 1


if __name__ == "__main__":
    sys.exit(main())
