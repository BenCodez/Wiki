"""Focused tests for the wiki source validator."""
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from validate_wiki import validate, without_fences

HEADER = "---\ntitle: Test\npublished: true\neditor: markdown\n---\n\n"


class WikiValidationTest(unittest.TestCase):
    def setUp(self):
        self.folder = tempfile.TemporaryDirectory()
        self.addCleanup(self.folder.cleanup)
        self.root = Path(self.folder.name)
        (self.root / ".wikijs").mkdir()
        (self.root / "VotingPlugin").mkdir()
        (self.root / "home.md").write_text(HEADER + "# Home\n")
        self.page = self.root / "VotingPlugin" / "Guide.md"
        self.page.write_text(HEADER + "[Home](/)\n")
        self.nav = self.root / ".wikijs" / "navigation.json"
        self.nav.write_text(json.dumps({"locales": [{"items": [
            {"id": "a", "targetType": "page", "target": "/en/VotingPlugin/Guide"}
        ]}]}))

    def test_valid_page_and_navigation(self):
        self.assertEqual([], validate(self.root, [self.page]))

    def test_missing_local_page(self):
        self.page.write_text(HEADER + "[Missing](/VotingPlugin/Missing)\n")
        self.assertTrue(any("broken internal link" in e for e in validate(self.root, [self.page])))

    def test_fenced_examples_are_ignored(self):
        self.page.write_text(HEADER + "~~~yaml\n[NotLink](/missing)\n~~~\n[Home](/)\n")
        self.assertEqual([], validate(self.root, [self.page]))
        self.assertNotIn("NotLink", without_fences(self.page.read_text()))

    def test_external_links_are_not_fetched(self):
        self.page.write_text(HEADER + "[External](https://example.org/a)\n[Anchor](#part)\n")
        self.assertEqual([], validate(self.root, [self.page]))

    def test_missing_nav_target(self):
        content = json.loads(self.nav.read_text())
        content["locales"][0]["items"][0]["target"] = "/en/VotingPlugin/Gone"
        self.nav.write_text(json.dumps(content))
        self.assertTrue(any("missing navigation page" in e for e in validate(self.root, [self.page])))

    def test_missing_frontmatter(self):
        self.page.write_text("# No metadata\n")
        self.assertTrue(any("missing YAML front matter" in e for e in validate(self.root, [self.page])))

    def test_reject_outside_repository(self):
        self.page.write_text(HEADER + "[Escape](../../../etc/passwd)\n")
        self.assertTrue(any("escapes repository" in e for e in validate(self.root, [self.page])))


if __name__ == "__main__":
    unittest.main()
