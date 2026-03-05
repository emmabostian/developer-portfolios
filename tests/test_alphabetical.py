import unittest
from src import alphabetical


class TestAlphabetical(unittest.TestCase):
    def test_trim_and_remove_duplicate(self):
        lines = [
            "- [Name ](https://example.com)\n",
            "- [Name](https://example.com)\n",
        ]
        out, removed = alphabetical.remove_exact_duplicate_links(lines)
        self.assertEqual(removed, 1)
        self.assertEqual(len(out), 1)
        # ensure the bracket text was trimmed in the output
        self.assertIn("[Name]", out[0])

    def test_case_sensitive(self):
        lines = [
            "- [Name](https://example.com)\n",
            "- [name](https://example.com)\n",
        ]
        out, removed = alphabetical.remove_exact_duplicate_links(lines)
        # case differs, should not be considered duplicate
        self.assertEqual(removed, 0)
        self.assertEqual(len(out), 2)

    def test_url_normalization(self):
        lines = [
            "- [Same](https://example.com/path/)\n",
            "- [Same](https://example.com/path)\n",
        ]
        out, removed = alphabetical.remove_exact_duplicate_links(lines)
        self.assertEqual(removed, 1)
        self.assertEqual(len(out), 1)

    def test_non_markdown_ignored(self):
        lines = [
            "## A\n",
            "- [A](https://a.com)\n",
            "Some text\n",
            "- [A](https://a.com)\n",
        ]
        out, removed = alphabetical.remove_exact_duplicate_links(lines)
        # duplicates are not adjacent (there's intervening text), so none removed
        self.assertEqual(removed, 0)
        self.assertEqual(len(out), 4)

    def test_multiple_adjacent_duplicates(self):
        lines = [
            "- [Foo](https://ex.com)\n",
            "- [Foo](https://ex.com)\n",
            "- [Foo](https://ex.com)\n",
        ]
        out, removed = alphabetical.remove_exact_duplicate_links(lines)
        # should collapse to a single kept entry
        self.assertEqual(removed, 2)
        self.assertEqual(len(out), 1)

    def test_remove_leading_single_letter_token(self):
        # leading single 'A' should be removed from bracketed link text
        line = "- [A John Doe](https://example.com)\n"
        out = alphabetical.convert_to_title_case(line)
        self.assertIn("[John Doe]", out)

        # lowercase 'a' should also be removed
        line2 = "- [a Jane](https://example.com)\n"
        out2 = alphabetical.convert_to_title_case(line2)
        self.assertIn("[Jane]", out2)

    def test_strip_aaa_prefix_token(self):
        # Only remove standalone 'Aaa' tokens.
        # 'Aaa' attached to a token should be preserved (title-cased by the function).
        line = "- [AaaJohn Doe](https://example.com)\n"
        out = alphabetical.convert_to_title_case(line)
        # 'AaaJohn' will be title-cased to 'Aaajohn' by str.title()
        self.assertIn("[Aaajohn Doe]", out)

        # when 'Aaa' is a separate token it should be removed
        line2 = "- [Aaa John Doe](https://example.com)\n"
        out2 = alphabetical.convert_to_title_case(line2)
        self.assertIn("[John Doe]", out2)

        # 'Aaa' inside a token should not be stripped under Option B
        line3 = "- [Foo AaaBar](https://example.com)\n"
        out3 = alphabetical.convert_to_title_case(line3)
        # 'AaaBar' -> 'Aaabar' after title-casing
        self.assertIn("[Foo Aaabar]", out3)


if __name__ == "__main__":
    unittest.main()
