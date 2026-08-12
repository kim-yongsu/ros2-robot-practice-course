# 여섯 단계가 하나의 Burger 기준선으로 이어진다

앞 단계의 정상 결과가 다음 단계의 입력이다. 중간 단계를 건너뛰면 같은 명령도 다른 시스템을 만든다.

| 단계 | 학습 범위 | 종료 능력 |
| ---: | --- | --- |
| 1 | 터미널·환경·Workspace | 명령 위치와 source를 설명한다. |
| 2 | Node·Topic·Service·Action | ROS graph 계약을 확인한다. |
| 3 | Domain·Pose·TF·URDF | 좌표·시간·모델을 읽는다. |
| 4 | Burger bringup·teleop | 저속 주행과 STOP을 검증한다. |
| 5 | Gazebo·SLAM·Localization·Nav2 | 시뮬레이션과 실물 증거를 분리한다. |
| 6 | 패키지·진단·증거·인수인계 | 수정·rollback·HOLD를 남긴다. |

**빠른 본선:** 터미널 → ROS graph → 좌표·TF → Burger bringup·teleop → Gazebo → SLAM → Localization → Nav2 → 증거와 인수인계

| 상태 | 정확한 뜻 | 허용 표현 |
| --- | --- | --- |
| PASS | 지정한 게이트를 실제로 통과 | 검사 범위 안에서 확인 |
| HOLD | 필수 입력·환경·실행이 없음 | 검증 필요 |
| FAIL | 계약 위반 또는 결과 불일치 | 수정 후 재검사 |
