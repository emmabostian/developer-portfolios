#!/usr/bin/env python3
"""Simple test runner for this repository.

Usage:
    python run_tests.py [-v]

This discovers tests under the `tests/` directory using unittest discovery
and returns a non-zero exit code if any tests fail.
"""
import sys
import unittest


def main(argv=None):
    argv = argv if argv is not None else sys.argv[1:]
    verbosity = 2 if ('-v' in argv or '--verbose' in argv) else 1

    loader = unittest.TestLoader()
    suite = loader.discover(start_dir='tests', pattern='test_*.py')
    runner = unittest.TextTestRunner(verbosity=verbosity)
    result = runner.run(suite)
    return 0 if result.wasSuccessful() else 1


if __name__ == '__main__':
    sys.exit(main())

