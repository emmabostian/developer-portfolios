import os
import unittest
from src import alphabetical


class TestIsWellFormedUrl(unittest.TestCase):
    def test_valid_urls(self):
        for url in (
            "https://example.com",
            "http://example.org/path",
            "https://sub.example.co.uk",
            "https://example.com:8080/path?q=1#frag",
            "https://example-with-hyphen.com",
        ):
            self.assertTrue(alphabetical.is_well_formed_url(url), url)

    def test_missing_slashes(self):
        self.assertFalse(alphabetical.is_well_formed_url("https:example.com"))

    def test_nested_markdown_link(self):
        self.assertFalse(
            alphabetical.is_well_formed_url("<[Portfolio-Link](https://example.com)>")
        )

    def test_non_http_scheme(self):
        self.assertFalse(alphabetical.is_well_formed_url("ftp://example.com"))

    def test_no_scheme(self):
        self.assertFalse(alphabetical.is_well_formed_url("example.com"))

    def test_no_tld(self):
        self.assertFalse(alphabetical.is_well_formed_url("https://localhost"))

    def test_embedded_whitespace(self):
        self.assertFalse(alphabetical.is_well_formed_url("https://exa mple.com"))

    def test_empty_host(self):
        self.assertFalse(alphabetical.is_well_formed_url("https://"))


class TestFindMalformedUrls(unittest.TestCase):
    def test_detects_missing_slashes(self):
        lines = ["- [Foo](https:example.com) [Full Stack]\n"]
        issues = alphabetical.find_malformed_urls(lines)
        self.assertEqual(issues, [(1, "Foo", "https:example.com")])

    def test_detects_nested_markdown_link(self):
        lines = ["- [Foo](<[Portfolio-Link](https://example.com)>) [Dev]\n"]
        issues = alphabetical.find_malformed_urls(lines)
        self.assertEqual(len(issues), 1)
        self.assertEqual(issues[0][:2], (1, "Foo"))

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