"""Run public-safe content checks for documentation and metadata."""

from __future__ import annotations

import re
from collections.abc import Iterable
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEXT_SUFFIXES = {".md", ".py", ".yml", ".yaml", ".toml", ".txt", ".cfg", ".cff"}
BLOCKED_PARTS = {
    ".git",
    ".venv",
    "venv",
    ".tox",
    ".nox",
    "node_modules",
    "__pycache__",
    ".pytest_cache",
    ".ruff_cache",
    ".mypy_cache",
    "_build",
    "generated",
}
PATH_PATTERNS = (
    r"/mnt/" + r"data/",
    r"[A-Za-z]:" + r"\\Users\\",
    "/" + "home" + "/" + r"[^/]+/",
)
SECRET_PATTERNS = (
    r"ghp_[A-Za-z0-9]{20,}",
    r"github_pat_[A-Za-z0-9_]{20,}",
    r"sk-[A-Za-z0-9]{20,}",
    r"AKIA[0-9A-Z]{16}",
    r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----",
)
TRACE_ID_PATTERN = re.compile(r"(?:\[)?B\d{2}-S\d{2}(?:\])?")


def public_text_files(root: Path) -> Iterable[Path]:
    """Yield public text files while excluding generated output."""
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if any(part in BLOCKED_PARTS for part in path.parts):
            continue
        if path.resolve() == Path(__file__).resolve():
            continue
        if path.suffix.lower() in TEXT_SUFFIXES or path.name == "LICENSE-CODE":
            yield path


def find_content_errors(root: Path = ROOT) -> list[str]:
    """Return private-path, secret, accessibility, and trace-ID findings."""
    errors: list[str] = []
    for path in public_text_files(root):
        text = path.read_text(encoding="utf-8", errors="replace")
        for pattern in PATH_PATTERNS:
            if re.search(pattern, text):
                errors.append(f"{path.relative_to(root)}: private path pattern {pattern!r}")
        for pattern in SECRET_PATTERNS:
            if re.search(pattern, text):
                errors.append(f"{path.relative_to(root)}: possible secret pattern")
        if path.suffix == ".md":
            for alt in re.findall(r"!\[([^\]]*)\]\(", text):
                if not alt.strip():
                    errors.append(f"{path.relative_to(root)}: empty image alt text")
            if TRACE_ID_PATTERN.search(text):
                errors.append(f"{path.relative_to(root)}: undefined production trace ID")
    return errors


def main() -> int:
    """Run content lint and return a shell-friendly exit code."""
    errors = find_content_errors()
    if errors:
        print("\n".join(errors))
        return 1
    print("content lint: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
