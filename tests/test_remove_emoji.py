import unittest
from src import alphabetical


class TestRemoveEmoji(unittest.TestCase):
    def test_remove_from_link_text(self):
        lines = ["- [Alice 😊](https://example.com)\n"]
        new_lines, removed = alphabetical.remove_emoji_from_lines(lines)
        self.assertEqual(removed, 1)
        # emoji removed and trailing space collapsed/trimmed
        self.assertIn("[Alice]", new_lines[0])

    def test_remove_from_bracket_desc(self):
        lines = ["- [Foo](https://x) [Dev 😄]\n"]
        new_lines, removed = alphabetical.remove_emoji_from_lines(lines)
        self.assertEqual(removed, 1)
        # emoji removed and trailing space collapsed/trimmed
        self.assertIn("[Dev]", new_lines[0])

    def test_remove_from_paren_desc(self):
        lines = ["- [Foo](https://x) (😄)\n"]
        new_lines, removed = alphabetical.remove_emoji_from_lines(lines)
        self.assertEqual(removed, 1)
        self.assertIn("()", new_lines[0])

    def test_no_emoji(self):
        lines = ["- [Alice](https://example.com)\n"]
        new_lines, removed = alphabetical.remove_emoji_from_lines(lines)
        self.assertEqual(removed, 0)
        self.assertEqual(new_lines, lines)


if __name__ == "__main__":
    unittest.main()

