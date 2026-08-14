---
title: 4. ISO·APT·GitHub·workspace의 계보를 분리한다
source_pdf_page: 8
canonical_language: ko
course_id: burger-v1
volume: 1
part: 1
lesson: 4
status: source-supported
---

<div class="course-progress-anchor" data-course-progress-anchor data-course-id="burger-v1" data-lesson-id="04" data-lesson-title="ISO·APT·GitHub·workspace의 계보를 분리한다"></div>

<p class="lesson-kicker">PART 1 · 환경 기준선 / LESSON 04</p>

# 4. ISO·APT·GitHub·workspace의 계보를 분리한다

운영체제 이미지, APT underlay, GitHub source, 로컬 workspace를 서로 다른 설치·삭제·rollback 층으로 관리한다.

<div class="lesson-meta-grid" role="list" aria-label="단원 정보">
  <div role="listitem"><strong>환경</strong><span>Ubuntu 22.04.5 · ROS 2 Humble</span></div>
  <div role="listitem"><strong>원문</strong><span>PDF 8쪽</span></div>
  <div role="listitem"><strong>예상 시간</strong><span>원문 미기재 · 직접 계획</span></div>
  <div role="listitem"><strong>검증 상태</strong><span>Source-supported / runtime 별도</span></div>
</div>

![APT underlay와 GitHub overlay에서 src·build·install·log의 역할과 삭제 전 확인사항을 비교한 도해.](/_static/generated/diagrams/burger/volume-1/figure-05.png)

## 학습 목표

- `src`, `build`, `install`, `log`의 역할을 구분한다.
- underlay에서 overlay로 이어지는 source·build 순서를 실행한다.
- 삭제 전 commit·branch·재빌드 가능성·현재 shell source 여부를 확인한다.

## 선수 조건

- Lesson 03의 Ubuntu 22.04.5·Humble 기준선
- 작업할 `~/turtlebot3_ws` 경로 확인

## 핵심 개념

| 위치 | 역할 | 지우기 전 확인 |
| --- | --- | --- |
| `src` | 수정하는 source | commit·branch·변경 파일 |
| `build` | 패키지별 중간 산출물 | 재빌드 가능 여부 |
| `install` | 실행 파일·환경 hook | 현재 shell source 여부 |
| `log` | 빌드 로그 | 첫 실패 package |

## 준비

- 현재 장비·shell·경로·ROS 배포판을 확인한다.
- 이 Lesson에서 필요한 실제 입력이 없으면 결과를 만들지 않고 `HOLD`로 남긴다.
- 명령과 관찰을 같은 실행 회차의 증거로 연결할 저장 위치를 준비한다.

## 실행

```bash
source /opt/ros/humble/setup.bash
cd ~/turtlebot3_ws
rosdep install --from-paths src --ignore-src -r -y
colcon build --symlink-install
source install/setup.bash
```

## 예상 결과

:::{admonition} 예상 결과의 경계
:class: expected-result
아래 항목은 원문이 제시한 판정 기준이다. 실제 장비·설치본의 출력 로그를 이 문서가 대신 만들지는 않는다.
:::

- underlay를 먼저 source하고 overlay를 build·source한다.
- 새 shell에서도 같은 순서로 package와 executable을 찾을 수 있다.

## 관찰 포인트

- 빌드 실패 시 전체 로그의 마지막 줄이 아니라 첫 실패 package를 찾는다.
- `install`을 지운 뒤 현재 shell이 이전 hook를 계속 들고 있지 않은지 본다.

## PASS / HOLD / FAIL

::::{grid} 1 1 3 3
:gutter: 2
:class-container: status-gate-grid

:::{grid-item-card} ✓ PASS
:class-item: status-pass
새 shell에서 underlay → overlay 순서를 재현해 package를 찾고 executable을 실행할 수 있다.
:::

:::{grid-item-card} ◇ HOLD
:class-item: status-hold
source·branch·변경 파일 또는 첫 실패 package가 확인되지 않는다.
:::

:::{grid-item-card} ✕ FAIL
:class-item: status-fail
ISO·APT·GitHub·workspace를 같은 층으로 취급해 무작정 삭제·재설치한다.
:::

::::

## STOP 조건

:::{danger}
정상 결과와 STOP 조건을 구분하지 못하면 다음 단계로 진행하지 않는다.
:::

## 실패·문제해결

- `src` 변경사항을 보존하지 않고 workspace 삭제
- overlay보다 먼저 또는 underlay 없이 source
- 첫 실패 package를 건너뛰고 뒤쪽 오류만 수정

첫 수정 전에 **마지막 PASS와 첫 FAIL**을 기록하고 한 번에 한 변수만 바꾼다.

## 증거 체크리스트

- [ ] workspace 경로와 branch·commit
- [ ] rosdep·colcon 명령과 첫 실패 또는 성공 결과
- [ ] 새 shell source 순서

## 확인 문제

**질문:** `install` 폴더가 존재하면 새 shell에서도 overlay가 자동 적용되는가?

:::{dropdown} 정답 확인
:class-container: knowledge-answer
아니다. 새 shell에서 underlay와 `install/setup.bash`를 다시 source해야 한다.
:::

## 실습 과제

workspace 네 폴더의 역할과 삭제 전 확인사항을 자신의 경로에 맞춰 기록하고 새 shell 재현 절차를 실행한다.


## 학습 완료

<div class="mark-complete-panel" data-course-mark-complete>
  <p>완료 표시는 이 브라우저의 localStorage에만 저장되며 서버로 전송되지 않는다.</p>
  <button type="button" class="mark-complete-button" data-mark-complete-button>Lesson 04 완료로 표시</button>
  <span class="progress-announcement" data-progress-announcement aria-live="polite"></span>
</div>
<noscript>JavaScript가 꺼져 있어도 본문·명령·이전/다음 학습은 그대로 사용할 수 있다.</noscript>

## 다음 단원

::::{grid} 1 1 2 2
:gutter: 2
:class-container: lesson-prev-next

:::{grid-item-card} ← 이전 학습
[Lesson 03 · Ubuntu 22.04.5·ROS 2 Humble 기준선을 고정한다](03-ubuntu-22-04-5-ros-2-humble-기준선을-고정한다.md)
:::

:::{grid-item-card} 다음 학습 →
[Lesson 05 · Package·Executable·Process·Node를 구분한다](05-package-executable-process-node를-구분한다.md)
:::

::::
