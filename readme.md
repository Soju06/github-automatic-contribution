# 깃허브 자동 기여

초록색으로 채우고 싶지만 올릴게 없어서 만든 쓰레기.

## Getting started on Windows

* 시작하기 전에

  파이썬 3.7.9로 작성되었습니다.

  단순히 git 명령어로 만들었기 때문에 외부 종속성은 없습니다.

* 저장소 복제하기

  ```shell
  git clone https://github.com/Soju06/github-automatic-contribution.git
  cd github-automatic-contribution
  ```

* 자신의 github 원격 저장소 추가

  ```shell
  git remote remove origin # 복제한 원격 저장소 끊기
  git remote add origin https://github.com/Soju06/test-repos.git # 자신의 원격 저장소 주소 추가
  ```

* 로그인 후 자동 시작 옵션 설정하기

  ```sh
  # python 3.7.9
  V:\github-automatic-contribution> py add-task_scheduler.py
  깃헙 기여 작업 스케줄러 등록
  
  로그인 후 실행 딜레이 입력 (1M, 5M, 10M, 1H, 2H, def: 1M): 30M
  # Show UAC
  등록 성공.
  
  V:\github-automatic-contribution>
  ```

  ## 끝.



## Problem Solving

* 수동 기여 방법

  ```shell
  py garbage-generator.py
  
  ...
  ...
  ...
  
  done.
  ```

* 작업 제거 방법

  ```shell
  V:\github-automatic-contribution> py remove-task_scheduler.py
  목록 불러오는중...
  항목 찾는중...
  garbage-generator_a9tJJ7
  garbage-generator_EtilHF
  garbage-generator_HdhcYb
  garbage-generator_M2e3fc
  항목 제거중...
  # Show UAC
  제거 성공.
  
  V:\github-automatic-contribution>
  ```



진짜 간단하게 만듬 킹갓 파이썬 ㄹㅇㅋㅋ