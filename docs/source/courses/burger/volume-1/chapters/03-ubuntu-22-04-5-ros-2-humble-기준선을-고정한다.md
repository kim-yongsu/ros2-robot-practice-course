---
title: "3. Ubuntu 22.04.5·ROS 2 Humble 기준선을 고정한다"
source_pdf_page: 7
canonical_language: ko
---

# 3. Ubuntu 22.04.5·ROS 2 Humble 기준선을 고정한다

같은 명령도 OS·ROS 배포판·source 순서·Domain·RMW가 다르면 다른 graph를 만든다. 문제 해결 전에 실행 환경을 기록한다.

![Ubuntu 22.04.5, ROS 2 Humble, workspace overlay, ROS_DOMAIN_ID와 RMW_IMPLEMENTATION을 위에서 아래로 확인하는 네 층 도해](/_static/generated/diagrams/burger/volume-1/figure-04.png)

Humble 실행 환경의 네 층

```bash
lsb_release -ds
printenv ROS_DISTRO
printenv ROS_DOMAIN_ID
printenv RMW_IMPLEMENTATION
which ros2
ros2 doctor --report
```

| 항목 | 잠금값 | 불일치 시 |
| --- | --- | --- |
| OS | Ubuntu 22.04.5 Jammy | 다음 단계 중지 |
| ROS_DISTRO | humble | source 계보 확인 |
| TURTLEBOT3_MODEL | burger | 실물·URDF·parameter 불일치 |
| Domain·RMW | 시험 회차별 기록 | 양쪽 PC 기준선 대조 |

변경 통제  branch·RMW·Domain·parameter를 동시에 바꾸지 않는다. 한 번에 한 변수만 바꾸고 전후 증거를 남긴다.
