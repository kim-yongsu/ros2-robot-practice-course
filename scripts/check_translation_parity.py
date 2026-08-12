"""Validate multilingual landing-page coverage and navigation metadata."""

from __future__ import annotations

from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
LANDING_PAGES = {
    "ko": "README.md",
    "en": "README.en.md",
    "zh-CN": "README.zh-CN.md",
}
MATURITY_LEVELS = {"L0", "L1", "L2", "L3"}


def find_translation_errors(root: Path = ROOT) -> list[str]:
    """Return missing or inconsistent translation metadata."""
    status = yaml.safe_load((root / "translation_status.yml").read_text(encoding="utf-8"))
    errors: list[str] = []
    if status.get("canonical_language") != "ko":
        errors.append("canonical language must be ko")
    if not str(status.get("canonical_version", "")).strip():
        errors.append("canonical_version is required")
    languages = status.get("languages", {})
    for code, file_name in LANDING_PAGES.items():
        path = root / file_name
        if not path.is_file():
            errors.append(f"missing landing page: {file_name}")
            continue
        row = languages.get(code, {})
        if row.get("maturity") not in MATURITY_LEVELS:
            errors.append(f"invalid translation maturity: {code}")
        if not row.get("reviewed_at"):
            errors.append(f"missing reviewed_at: {code}")
        text = path.read_text(encoding="utf-8")
        for target in LANDING_PAGES.values():
            if target != file_name and target not in text:
                errors.append(f"{file_name} does not link to {target}")
    return errors


def main() -> int:
    """Run the translation parity metadata check."""
    errors = find_translation_errors()
    if errors:
        print("\n".join(errors))
        return 1
    print("translation parity metadata: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
