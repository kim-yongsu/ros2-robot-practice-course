---
title: "9. 실제 Humble 증거 — C++ talker와 Python listener"
source_pdf_page: 13
canonical_language: ko
---

# 9. 실제 Humble 증거 — C++ talker와 Python listener

Node 구현 언어가 달라도 같은 interface contract를 사용하면 통신할 수 있다. 실제 원본 로그의 sequence와 timestamp를 짝지어 확인한다.

![왼쪽 C++ Publisher의 Hello World 1~7과 오른쪽 Python Subscriber의 수신 sequence가 대응하고 발행·수신 시각 차이가 표시된 증거 패널](/_static/generated/diagrams/burger/volume-1/figure-10.png)

C++ talker와 Python listener 실제 로그 대응

| 검사 | 결과 | 판정 |
| --- | --- | --- |
| sequence 대응 | 1~7 전부 일치 | message 전달 PASS |
| 시간 순서 | 모든 수신이 발행 뒤 | timestamp order PASS |
| 최대 관찰 지연 | 6.725 ms | 이 7 sample의 관찰값 |

| 파일 | 역할 | 보존 이유 |
| --- | --- | --- |
| 원본 log | 기계 판독 가능한 사실 | sequence 재검증 |
| 증거 패널 | 사람이 빠르게 이해 | 교육·리뷰 |
| 환경·명령·SHA | 실행 계보 | 재현·변조 확인 |

출처 경계  이 그림은 실제 cpp_talker.log와 python_listener.log를 읽기 좋게 재배치한 증거다. raw GUI screenshot으로 가장하지 않는다.
