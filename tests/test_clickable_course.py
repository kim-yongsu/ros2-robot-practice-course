"""Regression tests for the clickable ROS 2 course layer."""

from __future__ import annotations

import ast
import json
import subprocess
import sys
from pathlib import Path

import yaml

from scripts.course_contract_check import PART_MAPPING, REQUIRED_SECTIONS, run_checks

ROOT = Path(__file__).resolve().parents[1]
VOLUME = ROOT / "docs/source/courses/burger/volume-1"
CHAPTERS = VOLUME / "chapters"


def test_course_contract_check_passes() -> None:
    """The source-only publication contract reports no failures."""
    assert run_checks(ROOT) == []


def test_six_part_mapping_is_exact() -> None:
    """The locked six-PART map covers every Lesson exactly once."""
    values = [lesson for lessons in PART_MAPPING.values() for lesson in lessons]
    assert values == list(range(1, 26))
    assert [len(PART_MAPPING[str(number)]) for number in range(1, 7)] == [4, 5, 4, 4, 4, 4]


def test_source_map_and_front_matter_match() -> None:
    """Every chapter keeps its exact PDF page and PART provenance."""
    payload = yaml.safe_load((VOLUME / "source_map.yml").read_text(encoding="utf-8"))
    for row in payload["chapters"]:
        path = ROOT / row["markdown"]
        text = path.read_text(encoding="utf-8")
        assert f"source_pdf_page: {row['source_pdf_page']}" in text
        assert f"part: {row['part']}" in text


def test_each_lesson_has_required_learning_sections() -> None:
    """Every Lesson exposes goal, execution, verdict, evidence, and next learning."""
    for path in sorted(CHAPTERS.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        for section in REQUIRED_SECTIONS:
            assert f"## {section}" in text, (path, section)


def test_course_scripts_are_modular_and_local_only() -> None:
    """Progress storage, UI behavior, and accessibility stay in separate modules."""
    static = ROOT / "docs/source/_static/js"
    files = {
        "storage": static / "course-progress-storage.js",
        "progress": static / "course-progress.js",
        "a11y": static / "course-a11y.js",
    }
    assert all(path.exists() for path in files.values())
    combined = "\n".join(path.read_text(encoding="utf-8") for path in files.values())
    assert "window.localStorage" in combined
    assert "fetch(" not in combined
    assert "google-analytics" not in combined.lower()


def test_readme_and_pages_cta_are_absolute_and_actionable() -> None:
    """The repository front door points to the deployed course start."""
    text = (ROOT / "README.md").read_text(encoding="utf-8")
    assert "https://kim-yongsu.github.io/ros2-robot-practice-course/" in text
    assert "Burger 1권 온라인 강좌 시작" in text


def test_public_python_additions_follow_pep257() -> None:
    """New public Python modules and callables contain basic docstrings."""
    for path in (ROOT / "scripts/course_contract_check.py", Path(__file__)):
        tree = ast.parse(path.read_text(encoding="utf-8"))
        assert ast.get_docstring(tree), path
        for node in ast.walk(tree):
            if isinstance(
                node, ast.FunctionDef | ast.AsyncFunctionDef | ast.ClassDef
            ) and not node.name.startswith("_"):
                assert ast.get_docstring(node), f"{path}:{node.name}"


def test_cli_can_write_machine_readable_report(tmp_path: Path) -> None:
    """The contract CLI emits an auditable JSON report."""
    report = tmp_path / "course-contract.json"
    result = subprocess.run(
        [sys.executable, "scripts/course_contract_check.py", "--json-report", str(report)],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    payload = json.loads(report.read_text(encoding="utf-8"))
    assert payload == {"status": "PASS", "error_count": 0, "errors": []}
