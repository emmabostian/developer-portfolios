import os
import tempfile
import unittest
from src import alphabetical


class TestMainE2E(unittest.TestCase):
    def test_main_trims_and_writes_backup(self):
        orig = (
            "# Test README\n\n"
            "## A\n\n"
            "- [Name ](https://example.com)\n"
            "- [Name](https://example.com)\n"
            "- [Same](https://example.com/path/)\n"
            "- [Same](https://example.com/path)\n"
            "- [Other](https://other.com/)\n"
            "- [Foo](https://foo.com) [Full-Stack]\n"
        )

        with tempfile.TemporaryDirectory() as td:
            cwd = os.getcwd()
            try:
                os.chdir(td)
                # write README.md in tempdir
                with open("README.md", "w", encoding="utf-8") as f:
                    f.write(orig)

                # run the main function (it reads/writes README.md in cwd)
                alphabetical.main()

                # backup should exist and equal original content
                with open("README.md.bak", "r", encoding="utf-8") as b:
                    bak = b.read()
                self.assertEqual(bak, orig)

                # read the updated README.md
                with open("README.md", "r", encoding="utf-8") as f:
                    out = f.read()

                # bracket trailing space should be removed and duplicates collapsed
                self.assertEqual(out.count("[Name]"), 1)
                self.assertEqual(out.count("[Same]"), 1)

                # Full-Stack spelling should be normalized to "Full Stack"
                self.assertIn("Full Stack", out)

                # URL trailing slash normalized for the same link (should still be present
                # but duplicates removed): ensure base path exists
                self.assertIn("example.com/path", out)

            finally:
                os.chdir(cwd)


if __name__ == "__main__":
    unittest.main()
