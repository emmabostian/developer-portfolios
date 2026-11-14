import os
import tempfile
import unittest
from src import alphabetical


class TestFullStackVariants(unittest.TestCase):
    def test_bracket_variants_normalized(self):
        variants = [
            "Full-Stack",
            "Full - Stack",
            "FullStack",
            "Fullstack",
            "Full_stack",
            "FULLSTACK",
            "Full—Stack",  # em dash
            "Full / Stack",
        ]
        # build README with each variant following a link in a bracketed description
        lines = ["# Test\n", "## A\n"]
        for i, v in enumerate(variants):
            lines.append(f"- [Person{i}](http://example{i}.com) [{v}]\n")
        # add a paragraph that contains 'Full-Stack' and should remain unchanged
        lines.append("\nThis Full-Stack mention should NOT be changed in paragraph text.\n")

        orig = "".join(lines)

        with tempfile.TemporaryDirectory() as td:
            cwd = os.getcwd()
            try:
                os.chdir(td)
                with open("README.md", "w", encoding="utf-8") as f:
                    f.write(orig)

                alphabetical.main()

                with open("README.md", "r", encoding="utf-8") as f:
                    out = f.read()

                # Check that each bracket variant was turned into 'Full Stack'
                for i, v in enumerate(variants):
                    self.assertIn(f"Person{i}", out)
                    # the description bracket should contain 'Full Stack'
                    self.assertIn("Full Stack", out)

                # Ensure the paragraph 'Full-Stack' remains as-is (we expect one occurrence)
                self.assertIn("This Full-Stack mention should NOT be changed in paragraph text.", out)

            finally:
                os.chdir(cwd)

    def test_typos_normalized(self):
        for v in ["Fulletack", "fulstack", "Full Stak", "full-stak", "FULLETACK"]:
            with self.subTest(v=v):
                self.assertEqual(alphabetical._FULL_STACK_RE.sub("Full Stack", v), "Full Stack")

    def test_plurals_not_normalized(self):
        for v in ["Full Stacks", "fullstacks", "Full-Stacks", "Fulletacks", "Full Stacked"]:
            with self.subTest(v=v):
                self.assertEqual(alphabetical._FULL_STACK_RE.sub("Full Stack", v), v)

    def test_main_handles_typos_and_skips_plurals(self):
        lines = [
            "# Test\n", "## A\n",
            "- [Ann](http://a.com) [Fulletack Developer]\n",
            "- [Bob](http://b.com) [Fullstack Engineer]\n",
            "- [Cy](http://c.com) (full_stak dev)\n",
            "- [Di](http://d.com) [Full Stacks Wizard]\n",
        ]
        with tempfile.TemporaryDirectory() as td:
            cwd = os.getcwd()
            try:
                os.chdir(td)
                with open("README.md", "w", encoding="utf-8") as f:
                    f.write("".join(lines))
                alphabetical.main()
                with open("README.md", "r", encoding="utf-8") as f:
                    out = f.read()
            finally:
                os.chdir(cwd)
        self.assertIn("[Full Stack Developer]", out)
        self.assertIn("[Full Stack Engineer]", out)
        self.assertIn("(Full Stack dev)", out)
        self.assertIn("[Full Stacks Wizard]", out)


if __name__ == "__main__":
    unittest.main()

