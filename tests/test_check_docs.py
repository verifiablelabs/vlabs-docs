from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("check_docs", ROOT / "scripts" / "check_docs.py")
assert SPEC and SPEC.loader
checker = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(checker)


class DocsCheckTests(unittest.TestCase):
    def test_broken_relative_markdown_link_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "README.md").write_text("[missing](docs/missing.md)\n", encoding="utf-8")
            errors = checker.validate_docs(root)
        self.assertTrue(any("broken local link" in error for error in errors), errors)

    def test_fragment_and_external_links_are_not_treated_as_files(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "README.md").write_text(
                "[section](#section) [site](https://example.com) [mail](mailto:test@example.com)\n",
                encoding="utf-8",
            )
            self.assertEqual(checker.validate_docs(root), [])

    def test_common_secret_shapes_are_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            token = "gh" + "p_" + "A" * 36
            (root / "README.md").write_text(f"credential={token}\n", encoding="utf-8")
            errors = checker.validate_docs(root)
        self.assertTrue(any("secret-shaped" in error for error in errors), errors)

    def test_repository_docs_validate(self) -> None:
        self.assertEqual(checker.validate_docs(ROOT), [])


if __name__ == "__main__":
    unittest.main()
