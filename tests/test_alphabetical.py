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


    def test_validate_section_placement_single_misplaced(self):
        # Test that a single misplaced entry is moved to the correct section
        lines = [
            "## A\n",
            "\n",
            "- [Alice](https://alice.com)\n",
            "- [Zack](https://zack.com)\n",  # Should be moved to Z
            "\n",
            "## B\n",
            "\n",
            "- [Bob](https://bob.com)\n",
            "\n",
            "## Z\n",
            "\n",
            "- [Zoe](https://zoe.com)\n",
        ]
        out, moved = alphabetical.validate_section_placement(lines)
        self.assertEqual(moved, 1)

        # Check that Zack is no longer in section A
        out_str = ''.join(out)
        a_section = out_str.split('## B')[0]
        self.assertNotIn('Zack', a_section)

        # Check that Zack is now in section Z
        z_section = out_str.split('## Z')[1]
        self.assertIn('Zack', z_section)

    def test_validate_section_placement_multiple_misplaced(self):
        # Test that multiple misplaced entries are moved
        lines = [
            "## A\n",
            "\n",
            "- [Alice](https://alice.com)\n",
            "- [Bob Entry](https://bob.com)\n",  # Should be moved to B
            "- [Charlie Entry](https://charlie.com)\n",  # Should be moved to C
            "\n",
            "## B\n",
            "\n",
            "- [Ben](https://ben.com)\n",
            "\n",
        ]
        out, moved = alphabetical.validate_section_placement(lines)
        self.assertEqual(moved, 2)

    def test_validate_section_placement_accented_characters(self):
        # Test that accented characters are normalized correctly
        lines = [
            "## A\n",
            "\n",
            "- [Alice](https://alice.com)\n",
            "- [Étienne](https://etienne.com)\n",  # É should normalize to E
            "\n",
            "## E\n",
            "\n",
            "- [Emma](https://emma.com)\n",
        ]
        out, moved = alphabetical.validate_section_placement(lines)
        # Étienne should be moved from A to E
        self.assertEqual(moved, 1)

    def test_validate_section_placement_no_misplaced(self):
        # Test that correctly placed entries are not moved
        lines = [
            "## A\n",
            "\n",
            "- [Alice](https://alice.com)\n",
            "- [Andrew](https://andrew.com)\n",
            "\n",
            "## B\n",
            "\n",
            "- [Bob](https://bob.com)\n",
        ]
        out, moved = alphabetical.validate_section_placement(lines)
        self.assertEqual(moved, 0)

    def test_validate_section_placement_creates_new_section(self):
        # Test that a new section is created if needed
        lines = [
            "## A\n",
            "\n",
            "- [Alice](https://alice.com)\n",
            "- [Zoe Entry](https://zoe.com)\n",  # Should create section Z
            "\n",
            "## B\n",
            "\n",
            "- [Bob](https://bob.com)\n",
        ]
        out, moved = alphabetical.validate_section_placement(lines)
        self.assertEqual(moved, 1)

        # Check that section Z was created
        out_str = ''.join(out)
        self.assertIn('## Z', out_str)
        self.assertIn('Zoe Entry', out_str)


if __name__ == "__main__":
    unittest.main()
