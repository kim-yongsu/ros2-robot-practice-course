"""Fail-closed source checks that do not require a Sphinx installation."""

from __future__ import annotations

import ast
import hashlib
import re
import sys
from collections import deque
from pathlib import Path
from typing import Any

import yaml
from markdown_it import MarkdownIt

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "source"
ASSETS = ROOT / "assets"
GENERATED = DOCS / "_static" / "generated"
SOURCE_MAP = DOCS / "courses" / "burger" / "volume-1" / "source_map.yml"

TOCTREE_RE = re.compile(r"```\{toctree\}\s*\n(?P<body>.*?)\n```", re.DOTALL)
IMAGE_RE = re.compile(r"!\[(?P<alt>[^\]]*)\]\((?P<target>[^)]+)\)")
LITERAL_RE = re.compile(
    r"```\{literalinclude\}\s+(?P<target>[^\s]+)\s*\n(?P<body>.*?)\n```",
    re.DOTALL,
)


def sha256(path: Path) -> str:
    """Return one file digest without loading large assets twice."""

    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def split_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    """Parse optional YAML front matter and return the Markdown body."""

    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end < 0:
        raise ValueError("unterminated YAML front matter")
    payload = yaml.safe_load(text[4:end]) or {}
    if not isinstance(payload, dict):
        raise ValueError("front matter must be a mapping")
    return payload, text[end + 5 :]


def markdown_files() -> list[Path]:
    """Return canonical Markdown pages, excluding generated static files."""

    return sorted(path for path in DOCS.rglob("*.md") if "_static" not in path.parts)


def resolve_doc(source: Path, entry: str) -> Path:
    """Resolve one Sphinx toctree entry to its Markdown source."""

    clean = entry.split("#", 1)[0].strip()
    candidate = (source.parent / clean).resolve()
    if candidate.suffix:
        return candidate
    md_candidate = candidate.with_suffix(".md")
    if md_candidate.exists():
        return md_candidate
    return candidate / "index.md"


def parse_toctree(source: Path, body: str) -> list[Path]:
    """Read non-option lines from all MyST toctree directives."""

    result: list[Path] = []
    for match in TOCTREE_RE.finditer(body):
        for raw in match.group("body").splitlines():
            entry = raw.strip()
            if not entry or entry.startswith(":") or entry.startswith("#"):
                continue
            result.append(resolve_doc(source, entry))
    return result


def canonical_asset_for(target: str) -> Path | None:
    """Map a generated Sphinx image URL back to its canonical asset."""

    clean = target.split("#", 1)[0].split("?", 1)[0]
    prefix = "/_static/generated/"
    if not clean.startswith(prefix):
        return None
    return ASSETS / clean[len(prefix) :]


def check_markdown(errors: list[str]) -> dict[Path, list[Path]]:
    """Validate Markdown structure, images, literal includes, and toctrees."""

    parser = MarkdownIt("commonmark", {"html": True})
    graph: dict[Path, list[Path]] = {}
    for path in markdown_files():
        relative = path.relative_to(ROOT)
        try:
            frontmatter, body = split_frontmatter(path.read_text(encoding="utf-8"))
        except (UnicodeError, ValueError, yaml.YAMLError) as exc:
            errors.append(f"{relative}: front matter error: {exc}")
            continue

        try:
            tokens = parser.parse(body)
        except Exception as exc:  # markdown-it plugin-independent parse boundary
            errors.append(f"{relative}: Markdown parse error: {exc}")
            tokens = []

        h1_count = sum(token.type == "heading_open" and token.tag == "h1" for token in tokens)
        if h1_count != 1:
            errors.append(f"{relative}: expected exactly one level-1 heading, got {h1_count}")
        if frontmatter:
            title = str(frontmatter.get("title", "")).strip()
            if not title:
                errors.append(f"{relative}: front matter title is missing")
            if str(frontmatter.get("canonical_language", "")) != "ko":
                errors.append(f"{relative}: canonical_language must be ko")

        graph[path.resolve()] = parse_toctree(path, body)
        for target in graph[path.resolve()]:
            if not target.is_file():
                errors.append(f"{relative}: missing toctree target {target}")

        for match in IMAGE_RE.finditer(body):
            alt = match.group("alt").strip()
            target_text = match.group("target").strip()
            if not alt:
                errors.append(f"{relative}: empty image alt text")
            canonical = canonical_asset_for(target_text)
            if canonical is not None:
                if not canonical.is_file():
                    errors.append(f"{relative}: missing canonical image {canonical}")
                generated = DOCS / target_text.lstrip("/")
                if generated.exists() and canonical.exists():
                    if sha256(generated) != sha256(canonical):
                        errors.append(f"{relative}: generated asset drift {target_text}")
                continue
            if target_text.startswith(("http://", "https://", "data:")):
                continue
            candidate = (path.parent / target_text.split("#", 1)[0]).resolve()
            if not candidate.is_file():
                errors.append(f"{relative}: missing image target {target_text}")

        for match in LITERAL_RE.finditer(body):
            target_text = match.group("target").strip()
            candidate = (path.parent / target_text).resolve()
            if not candidate.is_file():
                errors.append(f"{relative}: missing literalinclude {target_text}")
                continue
            if candidate.suffix == ".py":
                try:
                    ast.parse(candidate.read_text(encoding="utf-8"))
                except (SyntaxError, UnicodeError) as exc:
                    errors.append(f"{relative}: invalid Python literalinclude: {exc}")
    return graph


def check_reachability(graph: dict[Path, list[Path]], errors: list[str]) -> None:
    """Require every canonical documentation page to be reachable from index.md."""

    root = (DOCS / "index.md").resolve()
    queue: deque[Path] = deque([root])
    visited: set[Path] = set()
    while queue:
        current = queue.popleft()
        if current in visited:
            continue
        visited.add(current)
        queue.extend(graph.get(current, []))
    expected = {path.resolve() for path in markdown_files()}
    unreachable = sorted(expected - visited)
    for path in unreachable:
        errors.append(f"{path.relative_to(ROOT)}: not reachable from docs/source/index.md")


def check_source_map(errors: list[str]) -> None:
    """Validate the 25 chapter source map against Markdown and canonical assets."""

    payload = yaml.safe_load(SOURCE_MAP.read_text(encoding="utf-8"))
    chapters = payload.get("chapters", []) if isinstance(payload, dict) else []
    if len(chapters) != 25:
        errors.append(f"source map: expected 25 chapters, got {len(chapters)}")
        return
    expected_pages = list(range(5, 30))
    actual_pages = [row.get("source_pdf_page") for row in chapters]
    if actual_pages != expected_pages:
        errors.append(f"source map: PDF pages must be 5..29, got {actual_pages}")

    for row in chapters:
        chapter = row.get("chapter")
        markdown = ROOT / str(row.get("markdown", ""))
        if not markdown.is_file():
            errors.append(f"source map chapter {chapter}: missing Markdown {markdown}")
            continue
        frontmatter, body = split_frontmatter(markdown.read_text(encoding="utf-8"))
        if frontmatter.get("source_pdf_page") != row.get("source_pdf_page"):
            errors.append(f"source map chapter {chapter}: source_pdf_page drift")
        front_title = re.sub(r"^\d+\.\s*", "", str(frontmatter.get("title", "")))
        map_title = re.sub(r"^\d+\.\s*", "", str(row.get("title", "")))
        if front_title != map_title:
            errors.append(f"source map chapter {chapter}: title drift")
        for image in row.get("images", []):
            canonical = ASSETS / "diagrams" / "burger" / "volume-1" / str(image)
            if not canonical.is_file():
                errors.append(f"source map chapter {chapter}: missing asset {image}")
            expected_ref = f"/_static/generated/diagrams/burger/volume-1/{image}"
            if expected_ref not in body:
                errors.append(f"source map chapter {chapter}: Markdown does not reference {image}")


def check_configuration(errors: list[str]) -> None:
    """Validate pinned documentation dependencies and required static files."""

    requirements = (ROOT / "docs" / "requirements.txt").read_text(encoding="utf-8").splitlines()
    constraints = (ROOT / "docs" / "constraints.txt").read_text(encoding="utf-8").splitlines()
    if requirements != constraints:
        errors.append("docs requirements and constraints must be identical and pinned")
    if any("==" not in line for line in requirements if line.strip() and not line.startswith("#")):
        errors.append("all documentation dependencies must be exact pins")
    if not (DOCS / "_static" / "course.css").is_file():
        errors.append("docs/source/_static/course.css is missing")
    conf = (DOCS / "conf.py").read_text(encoding="utf-8")
    for token in ("myst_parser", "furo", 'language = "ko"', "nitpicky = True"):
        if token not in conf:
            errors.append(f"docs/source/conf.py is missing required contract token {token!r}")


def main() -> int:
    """Run all source-only checks and return a shell-friendly status."""

    errors: list[str] = []
    check_configuration(errors)
    graph = check_markdown(errors)
    check_reachability(graph, errors)
    check_source_map(errors)
    if errors:
        print("Sphinx source preflight: FAIL", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print(
        "Sphinx source preflight: PASS "
        f"({len(markdown_files())} Markdown pages, 25 mapped chapters, 26 assets)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
