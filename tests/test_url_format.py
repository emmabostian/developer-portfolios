import os
import unittest
from src import alphabetical


class TestUrlFormat(unittest.TestCase):
    def test_detects_missing_slashes(self):
        lines = ["- [Foo](https:example.com) [Full Stack]\n"]
        issues = alphabetical.find_malformed_urls(lines)
        self.assertEqual(issues, [(1, "Foo", "https:example.com")])

    def test_accepts_valid_urls(self):
        lines = [
            "- [Foo](https://example.com)\n",
            "- [Bar](http://example.org/path) [Dev]\n",
        ]
        self.assertEqual(alphabetical.find_malformed_urls(lines), [])

    def test_ignores_non_entry_lines(self):
        lines = ["## A\n", "\n", "Some text about https:example.com\n"]
        self.assertEqual(alphabetical.find_malformed_urls(lines), [])

    def test_readme_has_no_malformed_urls(self):
        readme_path = os.path.join(os.path.dirname(__file__), "..", "README.md")
        with open(readme_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
        issues = alphabetical.find_malformed_urls(lines)
        self.assertEqual(issues, [], f"Malformed URLs found (line, name, url): {issues}")


if __name__ == "__main__":
    unittest.main()