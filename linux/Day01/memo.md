# day01 
# linux
- 기본 명령 구조 
  - sudo : 관리자 메뉴 
  - commandName option input

- 스탠다드 데이터 스트림 
  - standard Input(0) - command - Standard Output(1) or Standard Error(2)
메뉴얼 페이지 
[] - 선택사항 
<> - 필수사항
… 반복사항
| 로 구분 - 중에 하나 사용 둘 다는 안됨 
- history : 명령 기록 보기 !
- ls : 디렉터리 안의 내용을 보는데 사용하는 명령어
- cat : 1(생략가능, 스탠다드 아웃풋)> asd.txt 로 스트림 변경 
  -  덮어쓰기됨 추가로 하려면 cat 1>> output.txt  꺽새 두개 하면 문서에 추가됨


- cut : --delimiter " " --fields 1  공백을 기준으로 나누고 첫 번째 데이터를 출력 
- which : 명령어 위치 알 수 있음

- tee : 파일에 표준 입력을 읽어서 기록하고 출력도 함

- Piping : 한 명령의 표준 출력을 다른 표준 입력에 연결하는 것 | 사용
  - a 커맨드의 아웃풋을 b 커맨드의 인풋으로 사용 
  - 리디렉션이 한번 일어나면 파이프라인 끊김 
  - 가능하게 하려면 Tee 명령어 사용 데이터 스트리밍이 T 자 형태로 연결된다 해서 T
  - xargs : 스탠다드 인풋을 받지 않는 명령어에 스탠다드 인풋으로 넣어줌

- Aliases : 별칭  경로: 홈 디렉터리 .bash_aliases 파일에서 별칭 정의 앞에 닷 포함하고 파일 확장자 없어야됨 
  -  문법에 맞게 써야함 꼭꼭 띄어쓰기 주의********
-  manual : 매뉴얼 제공 man -k 특정 단어 