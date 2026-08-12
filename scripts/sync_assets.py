"""Synchronize canonical course assets into Sphinx static output."""

from __future__ import annotations

import hashlib
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "assets"
TARGET = ROOT / "docs/source/_static/generated"


def sha256(path: Path) -> bytes:
    """Return a binary SHA-256 digest."""
    return hashlib.sha256(path.read_bytes()).digest()


def require_safe_target(root: Path, target: Path) -> None:
    """Reject deletion outside the approved generated-static path."""
    expected = (root / "docs/source/_static/generated").resolve()
    if target.resolve() != expected:
        raise RuntimeError(f"Unsafe asset target: {target}")


def synchronize_assets(source: Path, target: Path) -> int:
    """Replace generated assets and verify byte-for-byte equality."""
    require_safe_target(ROOT, target)
    if target.exists():
        shutil.rmtree(target)
    shutil.copytree(source, target)
    count = 0
    for source_path in source.rglob("*"):
        if not source_path.is_file():
            continue
        relative = source_path.relative_to(source)
        target_path = target / relative
        if sha256(source_path) != sha256(target_path):
            raise RuntimeError(f"asset sync mismatch: {relative}")
        count += 1
    return count


def main() -> int:
    """Run the canonical asset synchronization."""
    count = synchronize_assets(SOURCE, TARGET)
    print(f"synced {count} assets")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
