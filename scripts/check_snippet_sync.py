"""Verify that chapter 21 includes the tested example source once."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHAPTER_ROOT = ROOT / "docs/source/courses/burger/volume-1/chapters"
EXPECTED_TARGET = "../../../../../../examples/burger/volume1/navigate_to_pose_client.py"


def validate_snippet_contract(root: Path = ROOT) -> list[str]:
    """Return snippet synchronization errors."""
    chapter = next((root / CHAPTER_ROOT.relative_to(ROOT)).glob("21-*.md"))
    text = chapter.read_text(encoding="utf-8")
    errors: list[str] = []
    if EXPECTED_TARGET not in text or "{literalinclude}" not in text:
        errors.append("chapter 21 is not linked to the tested example source")
    if "class NavigateToPoseClient" in text:
        errors.append("copied code detected in chapter 21")
    return errors


def main() -> int:
    """Run the snippet synchronization check."""
    errors = validate_snippet_contract()
    if errors:
        print("\n".join(errors))
        return 1
    print("snippet sync contract: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
