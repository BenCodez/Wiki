import importlib.util
import unittest
from pathlib import Path

source = Path(__file__).resolve().parents[1] / "generate_command_reference.py"
spec = importlib.util.spec_from_file_location("generate_command_reference", source)
parser = importlib.util.module_from_spec(spec)
spec.loader.exec_module(parser)


class SourceDocumentationTest(unittest.TestCase):
    def test_constructor_literals(self):
        code = 'new CommandHandler(plugin, new String[] { "Reload" }, "Vote.Reload|" + adminPerm, "Reload")'
        rows = parser.extract(code, "CommandLoader.java", lambda pos: "/av")
        self.assertEqual("Reload", rows[0]["args"])
        self.assertEqual("Vote.Reload|VotingPlugin.Admin", rows[0]["permission"])
        self.assertFalse(rows[0]["dynamic"])

    def test_dynamic_tokens_are_marked(self):
        code = 'new CommandHandler(plugin, new String[] { "Top", top.toString() }, "VotingPlugin.Admin", "Top")'
        rows = parser.extract(code, "CommandLoader.java", lambda pos: "/av")
        self.assertTrue(rows[0]["dynamic"])
        self.assertIn("<top.toString()>", rows[0]["args"])

    def test_generated_reference_contains_no_source_code_links(self):
        code = 'new CommandHandler(plugin, new String[] { "Reload" }, "Vote.Reload|" + adminPerm, "Reload")'
        rows = parser.extract(code, "CommandLoader.java", lambda pos: "/av")
        output = parser.render(rows)
        self.assertIn("| Command | Permission | Description |", output)
        self.assertIn("/av Reload", output)
        self.assertNotIn("| Source |", output)
        self.assertNotIn("github.com/BenCodez/VotingPlugin/blob/", output)

    def test_dynamic_source_expressions_not_advertised_as_commands(self):
        code = 'new CommandHandler(plugin, new String[] { "Top", top.toString() }, "Vote.Top", "Top")'
        rows = parser.extract(code, "CommandLoader.java", lambda pos: "/vote")
        output = parser.render(rows)
        self.assertNotIn("top.toString()", output)
        self.assertIn("omits 1 dynamically constructed", output)

    def test_signature_change_is_not_silent(self):
        with self.assertRaises(ValueError):
            parser.extract("new CommandHandler(unexpected)", "CommandLoader.java", lambda pos: "/vote")


if __name__ == "__main__":
    unittest.main()
