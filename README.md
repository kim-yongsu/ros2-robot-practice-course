<p align="right">
  <strong>한국어</strong> ·
  <a href="README.en.md">English</a> ·
  <a href="README.zh-CN.md">简体中文</a>
</p>

# ROS 2 로봇 실습 강좌

ROS 2 로봇 실습을 **Burger · Waffle Pi · Waffle Pi Tank · C2 6축 MoMa**의 강좌 구조로 정리하는 저장소다.

현재 출판 후보가 준비된 범위는 **TurtleBot3 Burger 1권**이다. 나머지 강좌는 완료 자료가 들어오기 전까지 준비 중으로 표시한다.

## 30초 입구

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r docs/requirements.txt -c docs/constraints.txt
python scripts/sync_assets.py
sphinx-build -W --keep-going -b html docs/source docs/_build/html
python -m pytest -q
```

온라인 교재 source는 [`docs/source`](docs/source/index.md), 실제 예제는 [`examples`](examples/README.md), 재현 검사는 [`tests`](tests/)에 있다.

## 현재 상태

| 영역 | 상태 |
| --- | --- |
| Burger 1권 한국어 교재 | 출판 후보 |
| Waffle Pi | 준비 중 |
| Waffle Pi Tank | 준비 중 |
| C2 · 6축 MoMa | 준비 중 |
| 완전한 ROS package source | HOLD — 공개 입력 미완료 |
| 실제 Humble `colcon build/test` | HOLD |
| Gazebo·Nav2·실물 Burger 통합 | HOLD |
| 공개 라이선스·관리자 identity | 결정 필요 |

## 단일 진실원

마이그레이션 이후 한국어 MyST source가 교재의 정본이다. DOCX와 PDF는 source snapshot 및 Release asset으로만 다룬다. 예제 코드는 문서에 복사하지 않고 실제 파일을 포함한다.

## 비공식 자료

이 저장소는 Open Robotics, ROS 프로젝트 또는 ROBOTIS의 공식 문서가 아니다. 이름과 표장에 관한 자세한 내용은 [`TRADEMARKS.md`](TRADEMARKS.md)를 확인한다.
