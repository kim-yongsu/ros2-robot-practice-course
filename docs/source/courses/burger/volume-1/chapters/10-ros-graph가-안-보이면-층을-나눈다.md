---
title: 10. ROS graph가 안 보이면 층을 나눈다
source_pdf_page: 14
canonical_language: ko
course_id: burger-v1
volume: 1
part: 3
lesson: 10
status: source-supported
---

<div class="course-progress-anchor" data-course-progress-anchor data-course-id="burger-v1" data-lesson-id="10" data-lesson-title="ROS graph가 안 보이면 층을 나눈다"></div>

<p class="lesson-kicker">PART 3 · 발견·좌표·TF·URDF / LESSON 10</p>

# 10. ROS graph가 안 보이면 층을 나눈다

ping 하나로 ROS 통신을 판정하지 않고 환경 → 네트워크 → 발견 → interface 순서로 첫 실패 계층을 찾는다.

<div class="lesson-meta-grid" role="list" aria-label="단원 정보">
  <div role="listitem"><strong>환경</strong><span>Ubuntu 22.04.5 · ROS 2 Humble</span></div>
  <div role="listitem"><strong>원문</strong><span>PDF 14쪽</span></div>
  <div role="listitem"><strong>예상 시간</strong><span>원문 미기재 · 직접 계획</span></div>
  <div role="listitem"><strong>검증 상태</strong><span>Source-supported / runtime 별도</span></div>
</div>

![ROS graph 발견 문제를 환경·네트워크·발견·interface 네 계층으로 분리한 진단 사다리.](/_static/generated/diagrams/burger/volume-1/figure-11.png)

## 학습 목표

- 환경·네트워크·발견·interface 계층을 순서대로 검사한다.
- Domain·RMW·daemon 문제와 namespace·remap 문제를 분리한다.
- 아래 계층이 PASS일 때만 다음 계층으로 이동한다.

## 선수 조건

- PART 1 환경 기준선
- PART 2 type·endpoint·QoS 조사 순서

## 핵심 개념

| 층 | 확인 | 실패하면 |
| --- | --- | --- |
| 환경 | source·ROS_DISTRO | 현재 터미널 환경부터 복구 |
| 네트워크 | IP·SSH 도달 | ROS 이전 연결 문제 |
| 발견 | Domain·localhost·RMW·daemon | 동일 계약과 daemon 재확인 |
| interface | endpoint·type·QoS·message | Node 존재와 실제 수신을 분리 |

## 준비

- 현재 장비·shell·경로·ROS 배포판을 확인한다.
- 이 Lesson에서 필요한 실제 입력이 없으면 결과를 만들지 않고 `HOLD`로 남긴다.
- 명령과 관찰을 같은 실행 회차의 증거로 연결할 저장 위치를 준비한다.

## 실행

```bash
printenv | grep -E 'ROS_DISTRO|ROS_DOMAIN_ID|ROS_LOCALHOST_ONLY|RMW_IMPLEMENTATION'
ip -br addr
ros2 daemon stop
ros2 node list
ros2 topic list -t
ros2 topic info --verbose /scan
```

## 예상 결과

:::{admonition} 예상 결과의 경계
:class: expected-result
아래 항목은 원문이 제시한 판정 기준이다. 실제 장비·설치본의 출력 로그를 이 문서가 대신 만들지는 않는다.
:::

- 현재 shell 환경값과 IP를 먼저 기록한다.
- daemon 재시작 뒤 Node·Topic·endpoint를 다시 조사한다.
- 첫 실패 계층과 마지막 PASS 계층을 분리해 남긴다.

## 관찰 포인트

- `ping` 또는 SSH 도달이 DDS discovery와 interface 호환을 대신하지 않는다.
- namespace·remap은 이름 계약이며 Domain·RMW discovery와 섞지 않는다.

## PASS / HOLD / FAIL

::::{grid} 1 1 3 3
:gutter: 2
:class-container: status-gate-grid

:::{grid-item-card} ✓ PASS
:class-item: status-pass
환경부터 interface까지 순차 검사하고 첫 실패 계층을 명시한다.
:::

:::{grid-item-card} ◇ HOLD
:class-item: status-hold
아래 계층이 아직 PASS하지 않았는데 위 계층 진단을 계속한다.
:::

:::{grid-item-card} ✕ FAIL
:class-item: status-fail
ping 성공 하나로 ROS graph 통신을 PASS하거나 여러 계층 설정을 동시에 변경한다.
:::

::::

## STOP 조건

:::{danger}
정상 결과와 STOP 조건을 구분하지 못하면 다음 단계로 진행하지 않는다.
:::

## 실패·문제해결

- 환경 확인 없이 daemon만 반복 재시작
- namespace 불일치를 네트워크 단절로 오판
- 토픽 이름과 실제 수신을 같은 증거로 취급

첫 수정 전에 **마지막 PASS와 첫 FAIL**을 기록하고 한 번에 한 변수만 바꾼다.

## 증거 체크리스트

- [ ] 환경변수·IP 출력
- [ ] daemon 전후 Node·Topic 목록
- [ ] endpoint·type·QoS·message 조사 결과와 첫 FAIL

## 확인 문제

**질문:** SSH가 성공하면 ROS 2 discovery도 성공했다고 볼 수 있는가?

:::{dropdown} 정답 확인
:class-container: knowledge-answer
아니다. 네트워크 도달 다음에 Domain·localhost·RMW·daemon과 interface를 별도로 확인해야 한다.
:::

## 실습 과제

현재 장비 두 대의 문제를 네 계층 표에 넣고 마지막 PASS와 첫 FAIL을 한 줄씩 적는다.


## 학습 완료

<div class="mark-complete-panel" data-course-mark-complete>
  <p>완료 표시는 이 브라우저의 localStorage에만 저장되며 서버로 전송되지 않는다.</p>
  <button type="button" class="mark-complete-button" data-mark-complete-button>Lesson 10 완료로 표시</button>
  <span class="progress-announcement" data-progress-announcement aria-live="polite"></span>
</div>
<noscript>JavaScript가 꺼져 있어도 본문·명령·이전/다음 학습은 그대로 사용할 수 있다.</noscript>

## 다음 단원

::::{grid} 1 1 2 2
:gutter: 2
:class-container: lesson-prev-next

:::{grid-item-card} ← 이전 학습
[Lesson 09 · 실제 Humble 증거 — C++ talker와 Python listener](09-실제-humble-증거-c-talker와-python-listener.md)
:::

:::{grid-item-card} 다음 학습 →
[Lesson 11 · PoseStamped는 frame·time·position·orientation 계약이다](11-posestamped는-frame-time-position-orientation-계약이다.md)
:::

::::
