---
title: "6. Topic·Service·Action·Parameter를 선택한다"
source_pdf_page: 10
canonical_language: ko
---

# 6. Topic·Service·Action·Parameter를 선택한다

통신 방식은 데이터가 계속 흐르는지보다 작업 계약으로 고른다. 누가 응답하고, 중간 상태와 취소가 필요한지를 먼저 정한다.

![Topic, Service, Action, Parameter를 비동기 message, 요청 응답, 장기 작업, Node 실행 설정으로 비교한 2×2 도해](/_static/generated/diagrams/burger/volume-1/figure-07.png)

ROS 2의 네 가지 핵심 interface

| 방식 | 계약 | Burger 예 |
| --- | --- | --- |
| Topic | 발행자·구독자의 비동기 message 교환 | /scan·/odom·/cmd_vel |
| Service | 한 request에 한 response | 상태 조회·짧은 명령 |
| Action | Goal·Feedback·Result·Cancel | NavigateToPose |
| Parameter | Node가 소유하는 실행 설정 | 속도·frame·plugin |

정확한 이해  Topic은 sensor처럼 주기적으로 발행할 수도 있고 사건이 생길 때만 발행할 수도 있다. 장시간 실행·진행 확인·취소가 필요하면 Action을 사용한다.

| Action 단계 | 클라이언트가 보는 것 | 서로 다른 실패 |
| --- | --- | --- |
| 서버 발견 | wait_for_server timeout | Server not found |
| Goal 응답 | accepted 여부 | Rejected |
| 실행 | Feedback·Cancel | 진행·취소 |
| 종료 | Result status | Succeeded·Aborted·Canceled |
