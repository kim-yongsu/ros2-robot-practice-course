"""Tests for the ROS 2 course repository publication contract."""

from __future__ import annotations

import ast
import re
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def test_twenty_five_burger_chapters_exist() -> None:
    """Burger Volume 1 contains exactly 25 ordered chapter files."""
    chapters = sorted((ROOT / "docs/source/courses/burger/volume-1/chapters").glob("*.md"))
    assert len(chapters) == 25
    assert [int(path.name[:2]) for path in chapters] == list(range(1, 26))


def test_source_map_matches_chapters() -> None:
    """The source map covers PDF pages 5 through 29 in order."""
    source_map = ROOT / "docs/source/courses/burger/volume-1/source_map.yml"
    payload = yaml.safe_load(source_map.read_text(encoding="utf-8"))
    assert len(payload["chapters"]) == 25
    assert [row["source_pdf_page"] for row in payload["chapters"]] == list(range(5, 30))
    assert payload["normalizations"][0]["type"] == ("remove_undefined_production_trace_ids")


def test_example_is_syntax_valid_and_has_main_guard() -> None:
    """The public NavigateToPose example parses and has a main guard."""
    path = ROOT / "examples/burger/volume1/navigate_to_pose_client.py"
    tree = ast.parse(path.read_text(encoding="utf-8"))
    guards = [
        node
        for node in ast.walk(tree)
        if isinstance(node, ast.If) and "__name__" in ast.unparse(node.test)
    ]
    assert guards


def test_example_distinguishes_accepted_and_success() -> None:
    """The example keeps accepted, success, and cancel states distinct."""
    text = (ROOT / "examples/burger/volume1/navigate_to_pose_client.py").read_text(encoding="utf-8")
    assert "Goal Accepted: execution has started (not yet success)." in text
    assert "STATUS_SUCCEEDED" in text
    assert "cancel_goal_async" in text


def test_documentation_uses_literalinclude() -> None:
    """Chapter 21 includes the tested source instead of copying it."""
    path = next((ROOT / "docs/source/courses/burger/volume-1/chapters").glob("21-*.md"))
    text = path.read_text(encoding="utf-8")
    assert "{literalinclude}" in text
    assert "navigate_to_pose_client.py" in text


def test_future_course_pages_are_honest() -> None:
    """Unwritten course modules remain explicitly marked as planned."""
    for folder in ("waffle-pi", "waffle-pi-tank", "c2-6axis-moma"):
        text = (ROOT / f"docs/source/courses/{folder}/index.md").read_text(encoding="utf-8")
        assert "상태: 준비 중" in text
        assert "완료되지 않은" in text


def test_no_empty_markdown_alt_text() -> None:
    """Every Markdown image has non-empty alternative text."""
    for path in (ROOT / "docs/source").rglob("*.md"):
        assert not re.search(r"!\[\s*\]\(", path.read_text(encoding="utf-8"))


def test_no_undefined_production_trace_ids() -> None:
    """Public chapters do not expose unexplained production trace IDs."""
    pattern = re.compile(r"(?:\[)?B\d{2}-S\d{2}(?:\])?")
    for path in (ROOT / "docs/source").rglob("*.md"):
        assert pattern.search(path.read_text(encoding="utf-8")) is None


def test_public_python_modules_have_docstrings() -> None:
    """Public Python modules and public callables follow PEP 257 basics."""
    roots = (ROOT / "examples", ROOT / "scripts", ROOT / "tests")
    for source_root in roots:
        for path in source_root.rglob("*.py"):
            tree = ast.parse(path.read_text(encoding="utf-8"))
            assert ast.get_docstring(tree), path
            for node in ast.walk(tree):
                if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                    if not node.name.startswith("_"):
                        assert ast.get_docstring(node), f"{path}:{node.name}"


def test_issue_form_uses_description() -> None:
    """The errata Issue Form uses the supported description field."""
    path = ROOT / ".github/ISSUE_TEMPLATE/errata.yml"
    payload = yaml.safe_load(path.read_text(encoding="utf-8"))
    assert "description" in payload
    assert "about" not in payload
    assert isinstance(payload["body"], list)


def test_sphinx_source_preflight_passes() -> None:
    """The fail-closed source-only Sphinx preflight passes."""
    result = subprocess.run(
        [sys.executable, str(ROOT / "scripts/sphinx_source_preflight.py")],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr
