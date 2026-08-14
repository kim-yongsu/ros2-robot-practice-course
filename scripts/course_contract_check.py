"""Validate the clickable ROS 2 course publication contract."""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections.abc import Iterable
from pathlib import Path

import yaml

EXPECTED_CHAPTERS = [
    "01-burger로-ros-2의-공통-기준선을-만든다.md",
    "02-터미널-linux-생존선을-먼저-확보한다.md",
    "03-ubuntu-22-04-5-ros-2-humble-기준선을-고정한다.md",
    "04-iso-apt-github-workspace의-계보를-분리한다.md",
    "05-package-executable-process-node를-구분한다.md",
    "06-topic-service-action-parameter를-선택한다.md",
    "07-이름보다-type-endpoint-qos-실제-값을-본다.md",
    "08-실제-humble-증거-turtlesim과-rqt_graph.md",
    "09-실제-humble-증거-c-talker와-python-listener.md",
    "10-ros-graph가-안-보이면-층을-나눈다.md",
    "11-posestamped는-frame-time-position-orientation-계약이다.md",
    "12-tf-edge마다-authority와-시간을-확인한다.md",
    "13-urdf와-robot_state_publisher의-책임을-나눈다.md",
    "14-cmd_vel과-실제-바퀴-사이의-경계를-나눈다.md",
    "15-bringup은-일곱-게이트를-통과한-뒤-실행한다.md",
    "16-첫-teleop은-0-01-m-s-한-단계와-즉시-정지로-시작한다.md",
    "17-gazebo-classic은-humble-가상-증거로만-사용한다.md",
    "18-slam은-지도-품질과-파일-계약까지-닫는다.md",
    "19-initial-pose는-scan-map-정합으로-판정한다.md",
    "20-nav2-goal은-네-게이트를-모두-통과한-뒤-보낸다.md",
    "21-navigatetopose는-모듈형-ament_python-패키지로-만든다.md",
    "22-문제는-처음-깨진-계층에서-자른다.md",
    "23-evidence-pack은-세-증거층을-한-run_id로-묶는다.md",
    "24-한-변수만-바꾸고-같은-시험으로-회귀한다.md",
    "25-조별-프로젝트는-재현-안전-증거로-완료한다.md",
]
PART_MAPPING = {
    "1": [1, 2, 3, 4],
    "2": [5, 6, 7, 8, 9],
    "3": [10, 11, 12, 13],
    "4": [14, 15, 16, 17],
    "5": [18, 19, 20, 21],
    "6": [22, 23, 24, 25],
}
REQUIRED_SECTIONS = (
    "학습 목표",
    "선수 조건",
    "핵심 개념",
    "준비",
    "실행",
    "예상 결과",
    "관찰 포인트",
    "PASS / HOLD / FAIL",
    "STOP 조건",
    "실패·문제해결",
    "증거 체크리스트",
    "확인 문제",
    "실습 과제",
    "학습 완료",
    "다음 단원",
)
PUBLIC_FORBIDDEN = (
    re.compile(r"(?:\[)?B\d{2}-S\d{2}(?:\])?"),
    re.compile(r"(?:internal|private)[ _-](?:audit|instruction|workflow)", re.IGNORECASE),
    re.compile(r"(?:agent|executor)[ _-](?:handoff|prompt)", re.IGNORECASE),
)
IMAGE_PATTERN = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")
HEADING_PATTERN = re.compile(r"^(#{1,6})\s+(.+?)\s*$")


def iter_public_markdown(root: Path) -> Iterable[Path]:
    """Yield public Markdown files that may be rendered or shown on GitHub."""
    yield root / "README.md"
    yield from sorted((root / "docs/source").rglob("*.md"))


def markdown_headings(text: str) -> list[tuple[int, str]]:
    """Return headings outside fenced code blocks."""
    headings: list[tuple[int, str]] = []
    in_fence = False
    for line in text.splitlines():
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        match = HEADING_PATTERN.match(line)
        if match:
            headings.append((len(match.group(1)), match.group(2)))
    return headings


def add_error(errors: list[str], condition: bool, message: str) -> None:
    """Append a message when a contract condition is false."""
    if not condition:
        errors.append(message)


def check_chapters(root: Path, errors: list[str]) -> None:
    """Check chapter count, order, metadata, sections, headings, and images."""
    chapter_dir = root / "docs/source/courses/burger/volume-1/chapters"
    chapters = sorted(chapter_dir.glob("*.md"))
    add_error(
        errors,
        [path.name for path in chapters] == EXPECTED_CHAPTERS,
        "25개 chapter 파일명·순서 불일치",
    )
    for number, path in enumerate(chapters, start=1):
        text = path.read_text(encoding="utf-8")
        for section in REQUIRED_SECTIONS:
            add_error(errors, f"## {section}" in text, f"{path}: 필수 section 누락: {section}")
        add_error(errors, f"source_pdf_page: {number + 4}" in text, f"{path}: 원문 PDF 쪽수 불일치")
        headings = markdown_headings(text)
        add_error(
            errors, sum(level == 1 for level, _ in headings) == 1, f"{path}: H1은 정확히 1개여야 함"
        )
        for previous, current in zip(headings, headings[1:], strict=False):
            add_error(
                errors,
                current[0] <= previous[0] + 1,
                f"{path}: heading 단계 건너뜀: {previous} -> {current}",
            )
        for alt, target in IMAGE_PATTERN.findall(text):
            add_error(errors, bool(alt.strip()), f"{path}: 빈 이미지 대체 텍스트")
            if target.startswith(("http://", "https://")):
                continue
            clean_target = target.split("#", 1)[0]
            image_path = (
                (root / "docs/source" / clean_target.lstrip("/"))
                if clean_target.startswith("/")
                else (path.parent / clean_target)
            )
            add_error(errors, image_path.resolve().exists(), f"{path}: 이미지 없음: {target}")


def check_source_map(root: Path, errors: list[str]) -> None:
    """Check one-to-one source provenance and locked PART membership."""
    path = root / "docs/source/courses/burger/volume-1/source_map.yml"
    payload = yaml.safe_load(path.read_text(encoding="utf-8"))
    chapters = payload.get("chapters", [])
    add_error(errors, len(chapters) == 25, "source_map chapter 수가 25가 아님")
    add_error(
        errors,
        [row.get("source_pdf_page") for row in chapters] == list(range(5, 30)),
        "source_map PDF 쪽수 불일치",
    )
    add_error(
        errors,
        payload.get("normalizations", [{}])[0].get("type")
        == "remove_unresolved_source_annotations",
        "source_map normalization 계약 불일치",
    )
    mapped = {str(number): [] for number in range(1, 7)}
    for row in chapters:
        mapped[str(row.get("part"))].append(row.get("chapter"))
    add_error(errors, mapped == PART_MAPPING, f"6 PART mapping 불일치: {mapped}")


def check_part_toctrees(root: Path, errors: list[str]) -> None:
    """Check every lesson is nested under exactly one locked PART landing page."""
    volume = root / "docs/source/courses/burger/volume-1"
    seen: list[str] = []
    for part_number, lessons in PART_MAPPING.items():
        part_dir = next(volume.glob(f"part-{int(part_number):02d}-*"), None)
        add_error(errors, part_dir is not None, f"PART {part_number} 폴더 없음")
        if part_dir is None:
            continue
        text = (part_dir / "index.md").read_text(encoding="utf-8")
        for lesson in lessons:
            stem = Path(EXPECTED_CHAPTERS[lesson - 1]).stem
            add_error(
                errors, stem in text, f"PART {part_number} toctree에 Lesson {lesson:02d} 누락"
            )
            seen.append(stem)
    add_error(errors, len(seen) == 25 and len(set(seen)) == 25, "Lesson 중복 또는 orphan 발생")


def check_public_content(root: Path, errors: list[str]) -> None:
    """Check public copy for internal leakage, empty alt text, and first CTA."""
    for path in iter_public_markdown(root):
        add_error(errors, path.exists(), f"공개 파일 없음: {path}")
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        for pattern in PUBLIC_FORBIDDEN:
            add_error(
                errors, pattern.search(text) is None, f"{path}: 내부 문구 노출: {pattern.pattern}"
            )
        add_error(errors, re.search(r"!\[\s*\]\(", text) is None, f"{path}: 빈 alt")
        add_error(errors, 'style="' not in text.lower(), f"{path}: 일회성 inline style 발견")
    readme = (root / "README.md").read_text(encoding="utf-8")
    home = (root / "docs/source/index.md").read_text(encoding="utf-8")
    add_error(errors, "Burger 1권 온라인 강좌 시작" in readme, "README 첫 학습 CTA 누락")
    add_error(errors, "Burger 1권 시작하기" in home, "강좌 홈 CTA 누락")
    add_error(errors, home.count("roadmap-card") == 6, "강좌 홈 6 PART roadmap card 불일치")


def check_progress_layer(root: Path, errors: list[str]) -> None:
    """Check local-only progress and graceful fallback contracts."""
    static = root / "docs/source/_static/js"
    storage = (static / "course-progress-storage.js").read_text(encoding="utf-8")
    progress = (static / "course-progress.js").read_text(encoding="utf-8")
    combined = storage + progress
    add_error(errors, "ros2-course:burger:v1:progress" in storage, "localStorage key 누락")
    add_error(errors, "window.localStorage" in storage, "localStorage adapter 누락")
    add_error(errors, "fetch(" not in combined, "진행률 계층에 네트워크 전송 발견")
    add_error(errors, "analytics" not in combined.lower(), "analytics 문구 발견")
    add_error(errors, "data-course-resume-link" in progress, "이어보기 selector 누락")
    for path in sorted((root / "docs/source/courses/burger/volume-1/chapters").glob("*.md")):
        text = path.read_text(encoding="utf-8")
        add_error(errors, "<noscript>" in text, f"{path}: JS fallback 누락")


def run_checks(root: Path) -> list[str]:
    """Run every local source-only gate and return all failures."""
    errors: list[str] = []
    check_chapters(root, errors)
    check_source_map(root, errors)
    check_part_toctrees(root, errors)
    check_public_content(root, errors)
    check_progress_layer(root, errors)
    return errors


def main() -> int:
    """Run the command-line publication contract validator."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--json-report", type=Path)
    args = parser.parse_args()
    root = args.root.resolve()
    errors = run_checks(root)
    payload = {
        "status": "PASS" if not errors else "FAIL",
        "error_count": len(errors),
        "errors": errors,
    }
    if args.json_report:
        args.json_report.parent.mkdir(parents=True, exist_ok=True)
        args.json_report.write_text(
            json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
    if errors:
        for error in errors:
            print(f"[FAIL] {error}")
        return 1
    print("[PASS] Clickable course source contract")
    return 0


if __name__ == "__main__":
    sys.exit(main())
