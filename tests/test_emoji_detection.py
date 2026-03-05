import unittest
from src import alphabetical


class TestEmojiDetection(unittest.TestCase):
    def test_link_text_with_emoji(self):
        line = "- [Alice 😊](https://example.com)\n"
        self.assertTrue(alphabetical.link_text_has_emoji(line))

    def test_no_emoji_in_link_text(self):
        line = "- [Alice](https://example.com)\n"
        self.assertFalse(alphabetical.link_text_has_emoji(line))

    def test_emoji_in_bracketed_description(self):
        line = "- [Foo](https://x) [Dev 😄]\n"
        self.assertTrue(alphabetical.emoji_adjacent_to_link(line))

    def test_emoji_in_parenthesized_description(self):
        line = "- [Foo](https://x) (😄)\n"
        self.assertTrue(alphabetical.emoji_adjacent_to_link(line))

    def test_zwj_sequence_detection(self):
        # family emoji formed with ZWJ should still be detected because they
        # contain pictographic codepoints
        line = "- [Family 👨\u200d👩\u200d👧](https://x)\n"
        self.assertTrue(alphabetical.link_text_has_emoji(line))

    def test_url_with_emoji_but_not_text(self):
        # emoji in the URL should not trigger link_text_has_emoji
        line = "- [Name](https://example.com/\U0001F600)\n"
        self.assertFalse(alphabetical.link_text_has_emoji(line))
        # but emoji_adjacent_to_link should also be False
        self.assertFalse(alphabetical.emoji_adjacent_to_link(line))


if __name__ == "__main__":
    unittest.main()

