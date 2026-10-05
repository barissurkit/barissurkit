import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
README = (ROOT / "README.md").read_text(encoding="utf-8")


class ProfileReadmeTest(unittest.TestCase):
    def test_first_line_is_a_markdown_title(self):
        first_line = README.splitlines()[0]
        self.assertRegex(first_line, r"^# \S")

    def test_title_is_followed_directly_by_a_plain_text_description(self):
        lines = README.splitlines()[1:]
        first = next((line.strip() for line in lines if line.strip()), "")
        self.assertFalse(first.startswith(("#", "<", "!", "[", "`", "-", "*")), first)
        self.assertGreaterEqual(len(first), 40)

    def test_code_fences_are_balanced(self):
        self.assertEqual(README.count("```") % 2, 0)

    def test_external_links_and_images_use_https(self):
        urls = re.findall(r"(?:\]\(|src=\")(https?://[^)\s\"]+)", README)
        self.assertTrue(urls, "README'de dış bağlantı bulunamadı")
        for url in urls:
            self.assertTrue(url.startswith("https://"), url)

    def test_local_links_point_to_existing_files(self):
        for target in re.findall(r"\]\((?!https?://|#|mailto:)([^)\s]+)\)", README):
            self.assertTrue((ROOT / target.split("#")[0]).exists(), target)

    def test_devlens_badge_points_to_this_profile(self):
        self.assertIn("devlens.barissurkit.com/u/barissurkit", README)
        self.assertIn("api/v1/badge/barissurkit.svg", README)


if __name__ == "__main__":
    unittest.main()
