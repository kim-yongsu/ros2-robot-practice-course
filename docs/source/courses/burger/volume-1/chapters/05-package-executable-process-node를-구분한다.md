---
title: 5. Package·Executable·Process·Node를 구분한다
source_pdf_page: 9
canonical_language: ko
course_id: burger-v1
volume: 1
part: 2
lesson: 5
status: source-supported
---

<div class="course-progress-anchor" data-course-progress-anchor data-course-id="burger-v1" data-lesson-id="05" data-lesson-title="Package·Executable·Process·Node를 구분한다"></div>

<p class="lesson-kicker">PART 2 · ROS 2 통신과 실행 증거 / LESSON 05</p>

# 5. Package·Executable·Process·Node를 구분한다

배포 묶음, 실행 진입점, OS process, ROS graph Node를 각각 다른 명령으로 확인한다.

<div class="lesson-meta-grid" role="list" aria-label="단원 정보">
  <div role="listitem"><strong>환경</strong><span>Ubuntu 22.04.5 · ROS 2 Humble</span></div>
  <div role="listitem"><strong>원문</strong><span>PDF 9쪽</span></div>
  <div role="listitem"><strong>예상 시간</strong><span>원문 미기재 · 직접 계획</span></div>
  <div role="listitem"><strong>검증 상태</strong><span>Source-supported / runtime 별도</span></div>
</div>

![Package에서 Executable·Process·Node로 이어지는 실행 관계와 각 확인 명령을 정리한 표.](/_static/generated/diagrams/burger/volume-1/figure-06.png)

## 학습 목표

- Package·Executable·Process·Node의 책임을 구분한다.
- 한 실행을 package에서 PID와 Node까지 추적한다.
- Executable 이름과 Node 이름이 항상 같지 않음을 설명한다.

## 선수 조건

- PART 1의 underlay·overlay source 재현

## 핵심 개념

| 단위 | 무엇인가 | 확인 명령 |
| --- | --- | --- |
| Package | source·설정·실행 파일의 배포 묶음 | `ros2 pkg list` · `ros2 pkg prefix` |
| Executable | package가 설치한 실행 진입점 | `ros2 pkg executables` |
| Process | OS가 PID·자원을 관리하는 실행 단위 | `ps` · `top` · `systemctl` |
| Node | ROS graph의 통신·parameter 주체 | `ros2 node list` · `ros2 node info` |

## 준비

- 현재 장비·shell·경로·ROS 배포판을 확인한다.
- 이 Lesson에서 필요한 실제 입력이 없으면 결과를 만들지 않고 `HOLD`로 남긴다.
- 명령과 관찰을 같은 실행 회차의 증거로 연결할 저장 위치를 준비한다.

## 실행

```bash
ros2 pkg executables demo_nodes_cpp
ros2 run demo_nodes_cpp talker
ros2 node list
ros2 node info /talker
ps -ef | grep '[t]alker'
```

## 예상 결과

:::{admonition} 예상 결과의 경계
:class: expected-result
아래 항목은 원문이 제시한 판정 기준이다. 실제 장비·설치본의 출력 로그를 이 문서가 대신 만들지는 않는다.
:::

- `demo_nodes_cpp` package의 executable을 확인한다.
- 실행 뒤 `/talker` Node와 OS process를 각각 찾는다.

## 관찰 포인트

- Executable 이름, Node 이름, process 명령줄을 별도 열로 기록한다.
- 한 process가 여러 Node를 포함하는 component container 가능성을 기억하되 현재 실행에서 실제로 확인한다.

## PASS / HOLD / FAIL

::::{grid} 1 1 3 3
:gutter: 2
:class-container: status-gate-grid

:::{grid-item-card} ✓ PASS
:class-item: status-pass
같은 실행을 Package·Executable·Process·Node 네 층에서 증거로 연결한다.
:::

:::{grid-item-card} ◇ HOLD
:class-item: status-hold
Node 이름이나 PID를 추정했지만 실제 명령 결과로 확인하지 않았다.
:::

:::{grid-item-card} ✕ FAIL
:class-item: status-fail
Package가 설치됐다는 사실만으로 Node가 실행 중이라고 판정한다.
:::

::::

## STOP 조건

:::{danger}
정상 결과와 STOP 조건을 구분하지 못하면 다음 단계로 진행하지 않는다.
:::

## 실패·문제해결

- Package와 Node를 같은 단위로 부름
- Node가 보이지 않는데 process 또는 executable 확인 없이 재설치
- Executable 이름을 Node 이름으로 고정 가정

첫 수정 전에 **마지막 PASS와 첫 FAIL**을 기록하고 한 번에 한 변수만 바꾼다.

## 증거 체크리스트

- [ ] `ros2 pkg executables` 결과
- [ ] `ros2 node info` 결과
- [ ] 해당 PID가 포함된 `ps` 결과

## 확인 문제

**질문:** 한 process가 반드시 한 Node만 실행하는가?

:::{dropdown} 정답 확인
:class-container: knowledge-answer
아니다. component container처럼 한 process가 여러 Node를 포함할 수 있으므로 실제 graph와 process를 각각 확인한다.
:::

## 실습 과제

talker 실행 전후로 네 단위의 증거를 수집하고 서로 같은 이름과 다른 이름을 표시한다.


## 학습 완료

<div class="mark-complete-panel" data-course-mark-complete>
  <p>완료 표시는 이 브라우저의 localStorage에만 저장되며 서버로 전송되지 않는다.</p>
  <button type="button" class="mark-complete-button" data-mark-complete-button>Lesson 05 완료로 표시</button>
  <span class="progress-announcement" data-progress-announcement aria-live="polite"></span>
</div>
<noscript>JavaScript가 꺼져 있어도 본문·명령·이전/다음 학습은 그대로 사용할 수 있다.</noscript>

## 다음 단원

::::{grid} 1 1 2 2
:gutter: 2
:class-container: lesson-prev-next

:::{grid-item-card} ← 이전 학습
[Lesson 04 · ISO·APT·GitHub·workspace의 계보를 분리한다](04-iso-apt-github-workspace의-계보를-분리한다.md)
:::

:::{grid-item-card} 다음 학습 →
[Lesson 06 · Topic·Service·Action·Parameter를 선택한다](06-topic-service-action-parameter를-선택한다.md)
:::

::::
