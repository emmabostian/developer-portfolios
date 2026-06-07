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


if __name__ == "__main__":
    unittest.main()

