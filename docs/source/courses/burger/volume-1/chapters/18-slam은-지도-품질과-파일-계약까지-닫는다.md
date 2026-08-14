---
title: 18. SLAM은 지도 품질과 파일 계약까지 닫는다
source_pdf_page: 22
canonical_language: ko
course_id: burger-v1
volume: 1
part: 5
lesson: 18
status: source-supported
---

<div class="course-progress-anchor" data-course-progress-anchor data-course-id="burger-v1" data-lesson-id="18" data-lesson-title="SLAM은 지도 품질과 파일 계약까지 닫는다"></div>

<p class="lesson-kicker">PART 5 · SLAM·Localization·Nav2 / LESSON 18</p>

# 18. SLAM은 지도 품질과 파일 계약까지 닫는다

Cartographer 실행, 저속 관측, 지도 품질 판정, YAML·image·SHA-256 보존을 하나의 폐루프로 본다.

<div class="lesson-meta-grid" role="list" aria-label="단원 정보">
  <div role="listitem"><strong>환경</strong><span>Ubuntu 22.04.5 · ROS 2 Humble</span></div>
  <div role="listitem"><strong>원문</strong><span>PDF 22쪽</span></div>
  <div role="listitem"><strong>예상 시간</strong><span>원문 미기재 · 직접 계획</span></div>
  <div role="listitem"><strong>검증 상태</strong><span>Source-supported / runtime 별도</span></div>
</div>

![SLAM 입력·관측·품질·YAML·PGM·SHA-256 저장을 하나의 폐루프로 묶은 도해.](/_static/generated/diagrams/burger/volume-1/figure-19.png)

## 학습 목표

- SLAM 입력·관측·품질·파일·증거 Gate를 구분한다.
- 이중 벽·전단·가짜 벽 없는 지도를 저장 대상으로 판정한다.
- YAML과 image를 같은 이름·버전·hash로 묶는다.

## 선수 조건

- Lesson 15 bringup Gate
- Lesson 16 저속 teleop·즉시 정지
- `/scan`·`/odom`·TF 안정 확인

## 핵심 개념

| 단계 | PASS 기준 | FAIL이면 |
| --- | --- | --- |
| 입력 | `/scan`·`/odom`·TF가 안정 | bringup·시간·frame 복구 |
| 관측 | 급가속 없이 모든 벽·코너 관측 | 속도 낮추고 재주행 |
| 품질 | 이중 벽·전단·가짜 벽 없음 | 저장 전 지도 재작성 |
| 파일 | YAML과 image가 같은 이름·버전 | 부분 교체 금지 |
| 증거 | 명령·RViz·파일 hash 보존 | PASS 대신 HOLD |

## 준비

- 현재 장비·shell·경로·ROS 배포판을 확인한다.
- 이 Lesson에서 필요한 실제 입력이 없으면 결과를 만들지 않고 `HOLD`로 남긴다.
- 명령과 관찰을 같은 실행 회차의 증거로 연결할 저장 위치를 준비한다.

## 실행

```bash
# Remote PC · bringup 정상 이후
export TURTLEBOT3_MODEL=burger
ros2 launch turtlebot3_cartographer cartographer.launch.py
ros2 run nav2_map_server map_saver_cli -f "$HOME/maps/classroom_v1"
sha256sum "$HOME/maps/classroom_v1.yaml" "$HOME/maps/classroom_v1.pgm"
```

## 예상 결과

:::{admonition} 예상 결과의 경계
:class: expected-result
아래 항목은 원문이 제시한 판정 기준이다. 실제 장비·설치본의 출력 로그를 이 문서가 대신 만들지는 않는다.
:::

- 입력 안정과 저속 관측을 확인한 뒤 지도를 저장한다.
- YAML과 PGM의 파일명·버전·SHA-256을 함께 기록한다.

## 관찰 포인트

- 파일 생성과 지도 품질 PASS를 같은 것으로 보지 않는다.
- 이중 벽·전단·가짜 벽을 저장 전에 판정한다.

## PASS / HOLD / FAIL

::::{grid} 1 1 3 3
:gutter: 2
:class-container: status-gate-grid

:::{grid-item-card} ✓ PASS
:class-item: status-pass
구조가 맞는 지도와 짝이 맞는 YAML·image·hash·실행 증거를 보존한다.
:::

:::{grid-item-card} ◇ HOLD
:class-item: status-hold
실물 교실 지도 품질 또는 Cartographer runtime을 직접 확인하지 않았다.
:::

:::{grid-item-card} ✕ FAIL
:class-item: status-fail
파일이 생성됐다는 사실만으로 지도 품질 PASS하거나 YAML과 image를 부분 교체한다.
:::

::::

## STOP 조건

:::{danger}
급가속 없이 저속으로 관측하고, 주행 경로와 정지 수단이 확보되지 않으면 실물 mapping을 시작하지 않는다.
:::

## 실패·문제해결

- 입력 불안정 상태에서 주행 반복
- 급가속으로 코너 관측 누락
- 이름이 같은 파일만 보고 hash 미보존

첫 수정 전에 **마지막 PASS와 첫 FAIL**을 기록하고 한 번에 한 변수만 바꾼다.

## 증거 체크리스트

- [ ] `/scan`·`/odom`·TF 기준선
- [ ] RViz 지도 품질 캡처
- [ ] 저장 명령과 YAML·PGM SHA-256

## 확인 문제

**질문:** `map_saver_cli`로 파일이 생기면 지도 품질도 PASS인가?

:::{dropdown} 정답 확인
:class-container: knowledge-answer
아니다. 이중 벽·전단·가짜 벽이 없는지 구조 품질을 별도로 판정해야 한다.
:::

## 실습 과제

현재 지도를 입력·관측·품질·파일·증거 다섯 Gate로 점검하고 확인하지 못한 항목은 HOLD로 남긴다.


## 학습 완료

<div class="mark-complete-panel" data-course-mark-complete>
  <p>완료 표시는 이 브라우저의 localStorage에만 저장되며 서버로 전송되지 않는다.</p>
  <button type="button" class="mark-complete-button" data-mark-complete-button>Lesson 18 완료로 표시</button>
  <span class="progress-announcement" data-progress-announcement aria-live="polite"></span>
</div>
<noscript>JavaScript가 꺼져 있어도 본문·명령·이전/다음 학습은 그대로 사용할 수 있다.</noscript>

## 다음 단원

::::{grid} 1 1 2 2
:gutter: 2
:class-container: lesson-prev-next

:::{grid-item-card} ← 이전 학습
[Lesson 17 · Gazebo Classic은 Humble 가상 증거로만 사용한다](17-gazebo-classic은-humble-가상-증거로만-사용한다.md)
:::

:::{grid-item-card} 다음 학습 →
[Lesson 19 · Initial Pose는 scan-map 정합으로 판정한다](19-initial-pose는-scan-map-정합으로-판정한다.md)
:::

::::
