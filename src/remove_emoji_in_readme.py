#!/usr/bin/env python3
"""Utility to remove emoji characters from link text and adjacent descriptions in README.md.

This module is placed inside `src/` so it can be executed either as a script
or as a package module. The import logic below tries common import paths so
it works in both execution modes.

Usage:
  python src/remove_emoji_in_readme.py        # dry-run (no write), prints summary
  python src/remove_emoji_in_readme.py --apply    # apply changes and write README.md (with backup README.md.bak)
  python -m src.remove_emoji_in_readme --apply   # run as package module
"""
import argparse
import os
import sys

# flexible import: prefer package import, fall back to module import when executed
try:
    from src import alphabetical as a
except Exception:
    try:
        import alphabetical as a
    except Exception:
        # Ensure project root is on path and try again
        sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
        from src import alphabetical as a


def main(argv=None):
    p = argparse.ArgumentParser(description="Remove emoji from README link text/descriptions")
    p.add_argument('--apply', action='store_true', help='Apply changes to README.md')
    p.add_argument('--no-backup', action='store_true', help="Don't write README.md.bak when applying")
    args = p.parse_args(argv)

    dry_run = not args.apply
    backup = not args.no_backup

    removed, orig_lines, new_lines = a.remove_emoji_from_readme(dry_run=dry_run, backup=backup)

    if removed == 0:
        print('No emoji found in link text/adjacent descriptions in README.md')
        return 0

    print(f'Removed {removed} emoji character(s) from README.md')
    # Print a few contextual diffs for user review (show changed lines)
    for i, (o, n) in enumerate(zip(orig_lines, new_lines), start=1):
        if o != n:
            print(f'Line {i}:')
            print('  -', o.rstrip())
            print('  +', n.rstrip())

    if not dry_run:
        print('Applied changes to README.md')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

