---
title: 11. PoseStamped는 frame·time·position·orientation 계약이다
source_pdf_page: 15
canonical_language: ko
course_id: burger-v1
volume: 1
part: 3
lesson: 11
status: source-supported
---

<div class="course-progress-anchor" data-course-progress-anchor data-course-id="burger-v1" data-lesson-id="11" data-lesson-title="PoseStamped는 frame·time·position·orientation 계약이다"></div>

<p class="lesson-kicker">PART 3 · 발견·좌표·TF·URDF / LESSON 11</p>

# 11. PoseStamped는 frame·time·position·orientation 계약이다

숫자만 읽지 않고 어느 frame에서 언제 측정한 위치와 회전인지 함께 해석한다.

<div class="lesson-meta-grid" role="list" aria-label="단원 정보">
  <div role="listitem"><strong>환경</strong><span>Ubuntu 22.04.5 · ROS 2 Humble</span></div>
  <div role="listitem"><strong>원문</strong><span>PDF 15쪽</span></div>
  <div role="listitem"><strong>예상 시간</strong><span>원문 미기재 · 직접 계획</span></div>
  <div role="listitem"><strong>검증 상태</strong><span>Source-supported / runtime 별도</span></div>
</div>

![PoseStamped의 frame·stamp·position·Quaternion 필드와 평면 yaw 대표 값을 설명한 도해.](/_static/generated/diagrams/burger/volume-1/figure-12.png)

## 학습 목표

- PoseStamped의 frame·stamp·position·orientation 필드를 구분한다.
- Quaternion의 `orientation.z` 하나를 yaw로 읽지 않는다.
- 평면 이동 단순식이 적용되는 조건과 대표 yaw 값을 설명한다.

## 선수 조건

- Lesson 10의 graph·interface 기준선
- PoseStamped message 또는 원문 예제

## 핵심 개념

| 필드 | 뜻 | 첫 검사 |
| --- | --- | --- |
| `header.frame_id` | 좌표값의 기준 frame | body·optical 축을 구분 |
| `header.stamp` | 측정 시각 | TF 시각과 호환되는지 확인 |
| `position x·y·z` | 해당 frame의 위치 | 단위와 축 방향 확인 |
| `orientation x·y·z·w` | Quaternion 회전 | `z` 하나를 yaw로 읽지 않음 |

**평면 이동에서 `roll=pitch=0`일 때만** `qz=sin(yaw/2)`, `qw=cos(yaw/2)`라는 단순식을 쓴다.

- Yaw 0° → `(qz, qw)=(0, 1)`
- Yaw 90° → `(0.7071, 0.7071)`
- Yaw 180° → `(1, 0)`
- Yaw -90° → `(-0.7071, 0.7071)`

## 준비

- 현재 장비·shell·경로·ROS 배포판을 확인한다.
- 이 Lesson에서 필요한 실제 입력이 없으면 결과를 만들지 않고 `HOLD`로 남긴다.
- 명령과 관찰을 같은 실행 회차의 증거로 연결할 저장 위치를 준비한다.

## 실행

이 Lesson은 비교·판정 중심이다. 아래 표와 관찰 항목을 자신의 실행 기록에 적용한다.

## 예상 결과

:::{admonition} 예상 결과의 경계
:class: expected-result
아래 항목은 원문이 제시한 판정 기준이다. 실제 장비·설치본의 출력 로그를 이 문서가 대신 만들지는 않는다.
:::

- frame과 stamp를 포함한 상태에서 position과 Quaternion을 해석한다.
- `position.z`, camera optical `z`, `orientation.z`를 서로 다른 값으로 구분한다.

## 관찰 포인트

- 현재 frame의 축 방향과 단위를 먼저 확인한다.
- TF 시각과 message stamp가 함께 해석 가능한지 본다.

## PASS / HOLD / FAIL

::::{grid} 1 1 3 3
:gutter: 2
:class-container: status-gate-grid

:::{grid-item-card} ✓ PASS
:class-item: status-pass
frame·time·position·orientation 네 계약을 모두 포함해 PoseStamped를 설명한다.
:::

:::{grid-item-card} ◇ HOLD
:class-item: status-hold
frame 또는 stamp를 잃어 position·Quaternion을 해석할 수 없다.
:::

:::{grid-item-card} ✕ FAIL
:class-item: status-fail
`orientation.z`를 그대로 yaw 각도로 읽거나 optical z와 position.z를 같은 값으로 취급한다.
:::

::::

## STOP 조건

:::{danger}
정상 결과와 STOP 조건을 구분하지 못하면 다음 단계로 진행하지 않는다.
:::

## 실패·문제해결

- frame_id를 생략한 좌표 비교
- Quaternion 네 성분 중 z 하나만 사용
- 평면 단순식을 roll·pitch가 있는 회전에 적용

첫 수정 전에 **마지막 PASS와 첫 FAIL**을 기록하고 한 번에 한 변수만 바꾼다.

## 증거 체크리스트

- [ ] PoseStamped 원문 또는 실제 message
- [ ] frame 축·단위 기록
- [ ] stamp와 TF 시간 호환 확인

## 확인 문제

**질문:** `orientation.z=0.7071`이면 항상 yaw 90°인가?

:::{dropdown} 정답 확인
:class-container: knowledge-answer
아니다. 원문의 단순 관계는 roll=pitch=0인 평면 회전 조건에서 qz와 qw를 함께 볼 때만 적용한다.
:::

## 실습 과제

PoseStamped 한 건에서 frame_id·stamp·position·orientation을 네 줄로 분해하고 해석에 필요한 미확인 항목은 HOLD로 표시한다.


## 학습 완료

<div class="mark-complete-panel" data-course-mark-complete>
  <p>완료 표시는 이 브라우저의 localStorage에만 저장되며 서버로 전송되지 않는다.</p>
  <button type="button" class="mark-complete-button" data-mark-complete-button>Lesson 11 완료로 표시</button>
  <span class="progress-announcement" data-progress-announcement aria-live="polite"></span>
</div>
<noscript>JavaScript가 꺼져 있어도 본문·명령·이전/다음 학습은 그대로 사용할 수 있다.</noscript>

## 다음 단원

::::{grid} 1 1 2 2
:gutter: 2
:class-container: lesson-prev-next

:::{grid-item-card} ← 이전 학습
[Lesson 10 · ROS graph가 안 보이면 층을 나눈다](10-ros-graph가-안-보이면-층을-나눈다.md)
:::

:::{grid-item-card} 다음 학습 →
[Lesson 12 · TF edge마다 authority와 시간을 확인한다](12-tf-edge마다-authority와-시간을-확인한다.md)
:::

::::
