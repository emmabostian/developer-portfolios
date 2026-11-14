#!/usr/bin/env python3
"""Simple test runner for this repo (moved to src).

Usage:
  python3 src/run_tests.py           # discover and run tests in ./tests with verbosity=2
  python3 src/run_tests.py -v 3      # set verbosity
  python3 src/run_tests.py --failfast # stop on first failure
"""
import argparse
import os
import sys
import unittest

# Tests do `from src import alphabetical`, so the repo root must be importable.
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)


def main(argv=None):
    parser = argparse.ArgumentParser(description="Run the test suite (unittest discovery)")
    parser.add_argument("-d", "--dir", default="tests", help="directory to discover tests in (default: tests)")
    parser.add_argument("-v", "--verbosity", type=int, default=2, help="test runner verbosity (default: 2)")
    parser.add_argument("--failfast", action="store_true", help="stop on first failure/error")
    args = parser.parse_args(argv)

    loader = unittest.TestLoader()
    try:
        start_dir = args.dir if os.path.isabs(args.dir) else os.path.join(REPO_ROOT, args.dir)
        suite = loader.discover(start_dir)
    except Exception as e:
        print(f"Error discovering tests in {args.dir}: {e}")
        return 2

    runner = unittest.TextTestRunner(verbosity=args.verbosity, failfast=args.failfast)
    result = runner.run(suite)

    # exit code: 0 on success, 1 on failures/errors, 2 on discovery error
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == "__main__":
    code = main()
    sys.exit(code)

