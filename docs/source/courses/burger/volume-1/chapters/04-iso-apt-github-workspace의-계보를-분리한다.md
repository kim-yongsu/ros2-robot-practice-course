---
title: "4. ISO·APT·GitHub·workspace의 계보를 분리한다"
source_pdf_page: 8
canonical_language: ko
---

# 4. ISO·APT·GitHub·workspace의 계보를 분리한다

운영체제 설치 이미지, 바이너리 패키지 주소, 소스 저장소, 로컬 workspace는 서로 다른 층이다. 삭제·재빌드·rollback 방법도 다르다.

![Ubuntu ISO에서 /opt/ros/humble underlay까지의 APT 계보와 GitHub source에서 workspace install overlay까지의 소스 빌드 계보를 나란히 비교한 도해](/_static/generated/diagrams/burger/volume-1/figure-05.png)

APT underlay와 GitHub overlay의 설치 계보

| 위치 | 역할 | 지우기 전 확인 |
| --- | --- | --- |
| src | 수정하는 소스 | commit·branch·변경 파일 |
| build | 패키지별 중간 산출물 | 재빌드 가능 여부 |
| install | 실행 파일·환경 hook | 현재 shell source 여부 |
| log | 빌드 로그 | 첫 실패 패키지 |

```bash
source /opt/ros/humble/setup.bash
cd ~/turtlebot3_ws
rosdep install --from-paths src --ignore-src -r -y
colcon build --symlink-install
source install/setup.bash
```

다음 단계 조건  package를 찾고 executable을 실행할 수 있으며, 새 shell에서 underlay → overlay 순서로 source했을 때 같은 결과가 나와야 한다.
