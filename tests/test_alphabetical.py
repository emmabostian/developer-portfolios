import unittest
from src import alphabetical


class TestAlphabetical(unittest.TestCase):
    def test_trim_and_remove_duplicate(self):
        lines = [
            "- [Name ](http://example.com)\n",
            "- [Name](http://example.com)\n",
        ]
        out, removed = alphabetical.remove_exact_duplicate_links(lines)
        self.assertEqual(removed, 1)
        self.assertEqual(len(out), 1)
        # ensure the bracket text was trimmed in the output
        self.assertIn("[Name]", out[0])

    def test_case_sensitive(self):
        lines = [
            "- [Name](http://example.com)\n",
            "- [name](http://example.com)\n",
        ]
        out, removed = alphabetical.remove_exact_duplicate_links(lines)
        # case differs, should not be considered duplicate
        self.assertEqual(removed, 0)
        self.assertEqual(len(out), 2)

    def test_url_normalization(self):
        lines = [
            "- [Same](http://example.com/path/)\n",
            "- [Same](http://example.com/path)\n",
        ]
        out, removed = alphabetical.remove_exact_duplicate_links(lines)
        self.assertEqual(removed, 1)
        self.assertEqual(len(out), 1)

    def test_non_markdown_ignored(self):
        lines = [
            "## A\n",
            "- [A](http://a.com)\n",
            "Some text\n",
            "- [A](http://a.com)\n",
        ]
        out, removed = alphabetical.remove_exact_duplicate_links(lines)
        # duplicates are not adjacent (there's intervening text), so none removed
        self.assertEqual(removed, 0)
        self.assertEqual(len(out), 4)

    def test_multiple_adjacent_duplicates(self):
        lines = [
            "- [Foo](http://ex.com)\n",
            "- [Foo](http://ex.com)\n",
            "- [Foo](http://ex.com)\n",
        ]
        out, removed = alphabetical.remove_exact_duplicate_links(lines)
        # should collapse to a single kept entry
        self.assertEqual(removed, 2)
        self.assertEqual(len(out), 1)


if __name__ == "__main__":
    unittest.main()

