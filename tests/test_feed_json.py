#!/usr/bin/env python3
"""
Test the feed.json generation functionality
"""

import json
import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from alphabetical import extract_portfolio_data


def test_extract_portfolio_data():
    """Test portfolio data extraction from markdown lines"""
    test_lines = [
        "- [Alice Smith](https://alice.com) [Full Stack Developer]\n",
        "- [Bob Jones](https://bob.dev)\n",
        "- [Carol White](https://carol.io) [UI/UX Designer | Frontend Dev]\n",
        "## Some Header\n",
        "Not a portfolio line\n",
        "- [Dave Brown](https://dave.com) []\n",  # Empty tagline
    ]

    portfolios = extract_portfolio_data(test_lines)

    # Test count
    assert len(portfolios) == 4, f"Expected 4 portfolios, got {len(portfolios)}"

    # Test first entry with tagline
    assert portfolios[0]['name'] == "Alice Smith"
    assert portfolios[0]['url'] == "https://alice.com"
    assert portfolios[0]['tagline'] == "Full Stack Developer"

    # Test entry without tagline
    assert portfolios[1]['name'] == "Bob Jones"
    assert portfolios[1]['url'] == "https://bob.dev"
    assert 'tagline' not in portfolios[1]

    # Test entry with complex tagline
    assert portfolios[2]['name'] == "Carol White"
    assert portfolios[2]['tagline'] == "UI/UX Designer | Frontend Dev"

    # Test entry with empty tagline (should not include tagline key)
    assert portfolios[3]['name'] == "Dave Brown"
    assert 'tagline' not in portfolios[3]

    print("✓ All portfolio extraction tests passed!")
    return True


def test_feed_json_structure():
    """Test that feed.json has valid structure"""
    try:
        with open('feed.json', 'r', encoding='utf-8') as f:
            portfolios = json.load(f)

        # Check it's a list
        assert isinstance(portfolios, list), "feed.json should contain a list"

        # Check we have entries
        assert len(portfolios) > 0, "feed.json should not be empty"

        # Check each entry has required fields
        for i, portfolio in enumerate(portfolios):
            assert 'name' in portfolio, f"Entry {i} missing 'name' field"
            assert 'url' in portfolio, f"Entry {i} missing 'url' field"
            assert isinstance(portfolio['name'], str), f"Entry {i} name should be string"
            assert isinstance(portfolio['url'], str), f"Entry {i} url should be string"

            # If tagline exists, it should be a string
            if 'tagline' in portfolio:
                assert isinstance(portfolio['tagline'], str), f"Entry {i} tagline should be string"

        print(f"✓ feed.json structure is valid ({len(portfolios)} entries)")
        return True
    except FileNotFoundError:
        print("✗ feed.json not found - run the script first")
        return False
    except json.JSONDecodeError as e:
        print(f"✗ feed.json is not valid JSON: {e}")
        return False


def main():
    """Run all tests"""
    print("Running feed.json tests...\n")

    results = []

    # Test extraction logic
    try:
        results.append(test_extract_portfolio_data())
    except AssertionError as e:
        print(f"✗ Portfolio extraction test failed: {e}")
        results.append(False)
    except Exception as e:
        print(f"✗ Unexpected error in extraction test: {e}")
        results.append(False)

    # Test feed.json structure
    try:
        results.append(test_feed_json_structure())
    except AssertionError as e:
        print(f"✗ Feed structure test failed: {e}")
        results.append(False)
    except Exception as e:
        print(f"✗ Unexpected error in structure test: {e}")
        results.append(False)

    # Summary
    print(f"\n{'='*50}")
    if all(results):
        print("✓ All tests passed!")
        return 0
    else:
        print(f"✗ {len([r for r in results if not r])} test(s) failed")
        return 1


if __name__ == "__main__":
    sys.exit(main())
