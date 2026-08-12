---
title: "10. ROS graph가 안 보이면 층을 나눈다"
source_pdf_page: 14
canonical_language: ko
---

# 10. ROS graph가 안 보이면 층을 나눈다

ping 한 번으로 ROS 통신을 증명하지 말고 환경·발견·인터페이스를 순서대로 자른다.

![환경, 네트워크, 발견, graph, 인터페이스, 이름 계약을 순서대로 확인하는 ROS 2 발견 진단 사다리.](/_static/generated/diagrams/burger/volume-1/figure-11.png)

LAYER-10-01 · 아래 계층이 PASS일 때만 다음 계층을 검사한다.

| 층 | 확인 | 실패하면 |
| --- | --- | --- |
| 환경 | source·ROS_DISTRO | 현재 터미널 환경부터 복구 |
| 네트워크 | IP·SSH 도달 | ROS 이전의 연결 문제 |
| 발견 | Domain·localhost·RMW·daemon | 동일 계약과 daemon 재확인 |
| 인터페이스 | endpoint·type·QoS·message | node 존재와 실제 수신을 분리 |

```bash
printenv | grep -E 'ROS_DISTRO|ROS_DOMAIN_ID|ROS_LOCALHOST_ONLY|RMW_IMPLEMENTATION'
ip -br addr
ros2 daemon stop
ros2 node list
ros2 topic list -t
ros2 topic info --verbose /scan
```

주의  namespace와 remap은 이름 계약이다. Domain·RMW처럼 discovery 계층의 문제와 섞지 않는다.
