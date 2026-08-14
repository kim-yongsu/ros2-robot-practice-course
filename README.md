<p align="right">
  <strong>한국어</strong> ·
  <a href="README.en.md">English</a> ·
  <a href="README.zh-CN.md">简体中文</a>
</p>

# ROS 2 로봇 실습 강좌

**GitHub 파일 트리가 아니라 온라인 교재에서 바로 시작한다.**

<p>
  <a href="https://kim-yongsu.github.io/ros2-robot-practice-course/"><strong>▶ Burger 1권 온라인 강좌 시작</strong></a>
  ·
  <a href="https://kim-yongsu.github.io/ros2-robot-practice-course/courses/burger/volume-1/start.html">처음부터 시작</a>
  ·
  <a href="https://kim-yongsu.github.io/ros2-robot-practice-course/courses/burger/volume-1/troubleshooting.html">문제 해결</a>
</p>

현재 공개 범위는 **TurtleBot3 Burger 1권 · ROS 2 Humble · 6 PART · 25 Lesson**이다. 목표·명령·예상 결과·STOP·증거·다음 학습을 한 Lesson 안에서 확인한다.

## 학습 경로

```text
환경 기준선 → 통신과 실행 증거 → 발견·좌표·TF·URDF
→ 실물 명령과 simulation → SLAM·Localization·Nav2
→ 진단·증거·회귀·프로젝트
```

Waffle Pi · Waffle Pi Tank · C2 6축 MoMa는 완료 source가 들어오기 전까지 **준비 중**으로 유지한다.

## 현재 상태

| 영역 | 상태 |
| --- | --- |
| Burger 1권 한국어 교재 | 출판 후보 |
| 온라인 교재 | Pages 배포 검증 대기 |
| Waffle Pi / Tank / C2 | 준비 중 |
| 완전한 ROS package source | HOLD — 공개 입력 미완료 |
| 실제 Humble `colcon build/test` | HOLD |
| Gazebo·Nav2·실물 Burger 통합 | HOLD |
| 문서 이용조건 | COPYRIGHT-DOCS.md 참조 |

## 개발·검증

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r docs/requirements.txt -c docs/constraints.txt -r requirements-dev.txt
python scripts/sync_assets.py
python scripts/course_contract_check.py
sphinx-build -W --keep-going -b html docs/source docs/_build/html
python -m pytest -q
```

온라인 교재 source는 [`docs/source`](docs/source/index.md), 실제 예제는 [`examples`](examples/README.md), 재현 검사는 [`tests`](tests/)에 있다.

## 단일 진실원

마이그레이션 이후 한국어 MyST source가 교재의 정본이다. DOCX와 PDF는 source snapshot 및 Release asset으로만 다룬다. 예제 코드는 문서에 복사하지 않고 실제 파일을 포함한다.

## 비공식 자료

이 저장소는 Open Robotics, ROS 프로젝트 또는 ROBOTIS의 공식 문서가 아니다. 이름과 표장에 관한 자세한 내용은 [`TRADEMARKS.md`](TRADEMARKS.md)를 확인한다.
