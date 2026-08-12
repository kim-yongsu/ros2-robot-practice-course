---
title: "18. SLAM은 지도 품질과 파일 계약까지 닫는다"
source_pdf_page: 22
canonical_language: ko
---

# 18. SLAM은 지도 품질과 파일 계약까지 닫는다

Cartographer를 실행한 뒤 저속으로 모든 코너를 관측하고, 구조가 맞는 지도만 YAML·image 한 버전으로 저장한다.

![bringup, Cartographer, 저속 teleop, 지도 품질 판정, map 저장, YAML·image·hash 잠금의 순차 흐름.](/_static/generated/diagrams/burger/volume-1/figure-19.png)

FLOW-18-01 · 지도 생성, 품질 판정, map.yaml·map.pgm·SHA-256 잠금을 하나의 폐루프로 본다.

| 단계 | PASS 기준 | FAIL이면 |
| --- | --- | --- |
| 입력 | /scan·/odom·TF가 안정 | bringup·시간·frame 복구 |
| 관측 | 급가속 없이 모든 벽·코너 관측 | 속도 낮추고 재주행 |
| 품질 | 이중 벽·전단·가짜 벽 없음 | 저장 전 지도 재작성 |
| 파일 | YAML과 image가 같은 이름·버전 | 부분 교체 금지 |
| 증거 | 명령·RViz·파일 hash 보존 | PASS 대신 HOLD |

```bash
# Remote PC · bringup 정상 이후
export TURTLEBOT3_MODEL=burger
ros2 launch turtlebot3_cartographer cartographer.launch.py
ros2 run nav2_map_server map_saver_cli -f "$HOME/maps/classroom_v1"
sha256sum "$HOME/maps/classroom_v1.yaml" "$HOME/maps/classroom_v1.pgm"
```

주의  파일이 생겼다는 사실은 지도 품질 PASS가 아니다. 실물 교실 지도 품질과 Cartographer runtime은 HOLD다.
