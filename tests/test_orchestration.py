"""Testes offline: estrutura, perfis e preservação das configurações."""

import importlib.util
import re
import tempfile
import tomllib
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("prepare_codex", ROOT / "scripts" / "prepare_codex.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class ConfigurationTests(unittest.TestCase):
    def test_all_agents_have_unique_names_and_supported_fields(self):
        names = set()
        for path in (ROOT / "codex" / "agents").glob("*.toml"):
            data = tomllib.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(path.stem, data["name"])
            self.assertNotIn(data["name"], names)
            names.add(data["name"])
            self.assertEqual(set(data), {"name", "description", "model", "model_reasoning_effort", "sandbox_mode", "developer_instructions"})
            self.assertIn(data["sandbox_mode"], {"read-only", "workspace-write"})
            self.assertIn(data["model_reasoning_effort"], {"low", "medium", "high"})
            self.assertTrue(data["description"])
            self.assertTrue(data["developer_instructions"])
            for skill in re.findall(r"\$([a-z0-9-]+)", data["developer_instructions"]):
                self.assertTrue((ROOT / "skills" / skill / "SKILL.md").is_file(), skill)
        self.assertEqual(len(names), 11)

    def test_review_agents_are_read_only(self):
        for name in ("triagem", "planejamento", "coordenacao", "qualidade", "arquitetura", "seguranca", "experiencia"):
            data = tomllib.loads((ROOT / "codex" / "agents" / f"{name}.toml").read_text(encoding="utf-8"))
            self.assertEqual(data["sandbox_mode"], "read-only")

    def test_main_config_does_not_override_permissions(self):
        data = tomllib.loads((ROOT / "codex" / "config.toml").read_text(encoding="utf-8"))
        self.assertEqual(set(data), {"model", "model_reasoning_effort", "agents"})
        self.assertTrue(data["agents"]["enabled"])
        self.assertLessEqual(data["agents"]["max_concurrent_threads_per_session"], 3)

    def test_skill_references_resolve(self):
        for path in (ROOT / "skills").rglob("*.md"):
            content = path.read_text(encoding="utf-8")
            for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", content):
                if "://" not in target and not target.startswith("#"):
                    self.assertTrue((path.parent / target.split("#")[0]).exists(), (path, target))

    def test_all_local_document_links_resolve(self):
        paths = [ROOT / "README.md", *(ROOT / "docs").rglob("*.md")]
        for path in paths:
            for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", path.read_text(encoding="utf-8")):
                if "://" not in target and not target.startswith("#"):
                    self.assertTrue((path.parent / target.split("#")[0]).exists(), (path, target))


class PreparationTests(unittest.TestCase):
    def test_profiles_change_all_models_without_changing_permissions(self):
        with tempfile.TemporaryDirectory() as temp:
            for profile in MODULE.PROFILES:
                target = MODULE.prepare(Path(temp) / profile, profile)
                self.assertEqual((target / "AGENTS.md").read_bytes(), (ROOT / "codex" / "AGENTS.md").read_bytes())
                for original in (ROOT / "codex").rglob("*.toml"):
                    relative = original.relative_to(ROOT / "codex")
                    before = tomllib.loads(original.read_text(encoding="utf-8"))
                    after = tomllib.loads((target / relative).read_text(encoding="utf-8"))
                    if profile == "equilibrado":
                        self.assertEqual(before, after)
                    if profile == "compatibilidade-5.5":
                        self.assertEqual(after["model"], "gpt-5.5")
                        self.assertEqual(after["model_reasoning_effort"], before["model_reasoning_effort"])
                        if "agents" in after:
                            self.assertEqual(after["agents"]["default_subagent_model"], "gpt-5.5")
                    if profile == "herdar":
                        self.assertNotIn("model", after)
                        self.assertNotIn("model_reasoning_effort", after)
                        if "agents" in after:
                            self.assertNotIn("default_subagent_model", after["agents"])
                            self.assertNotIn("default_subagent_reasoning_effort", after["agents"])
                    if "developer_instructions" in before:
                        self.assertEqual(before["developer_instructions"], after["developer_instructions"])
                        self.assertEqual(before["sandbox_mode"], after["sandbox_mode"])

    def test_existing_destination_is_preserved(self):
        with tempfile.TemporaryDirectory() as temp:
            destination = Path(temp) / "existing"
            destination.mkdir()
            sentinel = destination / "user.txt"
            sentinel.write_text("preservar", encoding="utf-8")
            with self.assertRaises(FileExistsError):
                MODULE.prepare(destination, "equilibrado")
            self.assertEqual(sentinel.read_text(encoding="utf-8"), "preservar")
            self.assertEqual(list(destination.iterdir()), [sentinel])

    def test_active_codex_paths_are_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            for directory in (".codex", ".agents", ".CODEX"):
                destination = Path(temp) / directory / "new"
                with self.assertRaises(ValueError):
                    MODULE.prepare(destination, "equilibrado")
                self.assertFalse(destination.exists())

    def test_unknown_profile_does_not_create_output(self):
        with tempfile.TemporaryDirectory() as temp:
            destination = Path(temp) / "new"
            with self.assertRaises(ValueError):
                MODULE.prepare(destination, "unknown")
            self.assertFalse(destination.exists())

    def test_invalid_source_does_not_create_output(self):
        with tempfile.TemporaryDirectory() as temp:
            destination = Path(temp) / "new"
            with self.assertRaises(FileNotFoundError):
                MODULE.prepare(destination, "equilibrado", Path(temp) / "missing")
            self.assertFalse(destination.exists())

    def test_model_assignment_inside_instructions_is_preserved(self):
        source = 'model = "gpt-5.6-sol"\ndeveloper_instructions = """\nmodel = "example"\n"""\n'
        result = tomllib.loads(MODULE.transform(source, "compatibilidade-5.5"))
        self.assertEqual(result["model"], "gpt-5.5")
        self.assertIn('model = "example"', result["developer_instructions"])


if __name__ == "__main__":
    unittest.main()
