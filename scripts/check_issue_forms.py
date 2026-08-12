"""Validate the minimal GitHub Issue Form contract."""

from __future__ import annotations

from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_TOP_LEVEL = {"name", "description", "body"}


def find_issue_form_errors(root: Path = ROOT) -> list[str]:
    """Return missing fields and legacy keys in Issue Forms."""
    errors: list[str] = []
    folder = root / ".github/ISSUE_TEMPLATE"
    for path in sorted(folder.glob("*.yml")):
        if path.name == "config.yml":
            continue
        payload = yaml.safe_load(path.read_text(encoding="utf-8"))
        if not isinstance(payload, dict):
            errors.append(f"{path.relative_to(root)}: form must be a mapping")
            continue
        missing = REQUIRED_TOP_LEVEL - payload.keys()
        if missing:
            errors.append(f"{path.relative_to(root)}: missing {sorted(missing)}")
        if "about" in payload:
            errors.append(f"{path.relative_to(root)}: use description, not about")
        if not isinstance(payload.get("body"), list):
            errors.append(f"{path.relative_to(root)}: body must be a list")
    return errors


def main() -> int:
    """Run the Issue Form validation."""
    errors = find_issue_form_errors()
    if errors:
        print("\n".join(errors))
        return 1
    print("issue forms: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
