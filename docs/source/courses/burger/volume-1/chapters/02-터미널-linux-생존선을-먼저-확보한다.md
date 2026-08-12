---
title: "2. 터미널·Linux 생존선을 먼저 확보한다"
source_pdf_page: 6
canonical_language: ko
---

# 2. 터미널·Linux 생존선을 먼저 확보한다

초보자의 첫 오류는 ROS가 아니라 경로·권한·shell·실행 위치에서 시작하는 경우가 많다. 명령이 어디서 실행되는지 먼저 고정한다.

![왼쪽 Remote PC에는 개발·RViz·teleop·SLAM·Nav2 명령, 오른쪽 Burger SBC에는 SSH·모델 선택·bringup·장치 확인·정상 종료 명령이 배치된 도해](/_static/generated/diagrams/burger/volume-1/figure-03.png)

Remote PC와 Burger SBC의 실행 책임

| 질문 | 정상 기준 | 첫 명령 |
| --- | --- | --- |
| 지금 어디에 있는가? | 예상한 작업 경로 | pwd |
| 어떤 파일이 있는가? | 오타 없는 파일·권한 | ls -la |
| ROS 환경이 적용됐는가? | ROS_DISTRO=humble | printenv ROS_DISTRO |
| process를 멈출 수 있는가? | Ctrl+C로 종료 | ps -ef / Ctrl+C |

STOP  실물 로봇이 예상과 다르게 움직이면 키보드 명령보다 물리 정지와 전원 차단 수단을 먼저 확보한다.

| 초보자 실수 | 바로잡기 | 확인 |
| --- | --- | --- |
| 프롬프트까지 붙여넣음 | $·사용자명·호스트는 제외 | 실제 명령만 실행 |
| 다른 PC에서 명령 실행 | Remote·SBC 표식을 먼저 확인 | hostname·pwd |
| source 없이 ROS 명령 | 현재 shell에 setup.bash 적용 | printenv ROS_DISTRO |
