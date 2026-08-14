"""Check relative Markdown links in the public repository candidate."""

from __future__ import annotations

import re
from collections.abc import Iterable
from pathlib import Path

LINK_PATTERN = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
ROOT = Path(__file__).resolve().parents[1]
BLOCKED_PARTS = {".git", "_build", "node_modules"}


def markdown_files(root: Path) -> Iterable[Path]:
    """Yield Markdown files outside generated build directories."""
    for path in root.rglob("*.md"):
        if not any(part in BLOCKED_PARTS for part in path.parts):
            yield path


def find_broken_links(root: Path) -> list[str]:
    """Return missing relative-link targets."""
    errors: list[str] = []
    for path in markdown_files(root):
        text = path.read_text(encoding="utf-8")
        for target in LINK_PATTERN.findall(text):
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            clean = target.split("#", 1)[0]
            if not clean:
                continue
            candidate = (path.parent / clean).resolve()
            if not candidate.exists():
                errors.append(f"{path.relative_to(root)} -> {target}")
    return errors


def main() -> int:
    """Run the relative-link check."""
    errors = find_broken_links(ROOT)
    if errors:
        print("broken relative links:\n" + "\n".join(errors))
        return 1
    print("relative links: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
