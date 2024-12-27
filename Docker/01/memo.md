# docker 1강 
웹 브라우저는 시크릿 탭으로 사용하면 좋음 - 캐시를 남기지 않아서 겹칠 일이 없다.

실행중인 모든 컨테이너 삭제하는 명령어
docker rm -f $(docker ps -aq)

도커란 컨테이너를 관리하기 위한 소프트웨어

컨테이너란? 
큰 서버를 효율적으로 나눠서 사용하기 위한 가상화 기술

서버, 가상화기술??

가상화 기술이란 ?
hypervisor vs container

애플리케이션 서버
서버의 개념
하드웨어와 하드웨어에서 실행되는 모든 소프트웨어까지 모두 포함하는 단어
문맥에 따라 다름

serve 접두어 제공하다 
제공하는 주체 
항상 요청애 대한 응답을 제공

서버에서 실행되는 소프트워에 따라 서버의 종류를 나눔
- 파일서버: 파일공유 소프트웨어
- db서버: dbms
- 웹서버: 소스코드를 통해 개발된 애플리케이션을 실행하는 소프트웨어 html 프론트 등 
- 웹애플리케이션 서버: 프로그래밍 언어로 개발된 서버 WAS


베어메탈 방식
서버를 구입 후 os를 설치 후 여러 소프트웨어를 실행 

하이퍼바이저, 컨테이너 방식이 같이 사용

실재 - 물리
가상 - 논리 

가상화 정의
물리적인 컴퓨팅 환경 내부에서 논리적으로 컴퓨팅 환경을 만드는 기술

가상화의 사용 이유

os 리소스 도 잡고 하나의 프로그램이 오류를 발생하면 연쇄적으로 발생할 수 있다
운영적인 환경이 멈추면 아주 큰 장애
때문에 소프트웨어를 여러 대로 사용하면 좋음
가상환경은 똑같은 os에 리소스를 직접 분배할 수 있다.

가상화를 하면 총 리소스는 늘어나지만 연쇄적 반응은 없어서 운영관리 측면에서 안정적

프로세스는 커널에 시스템 콜을 보내서 하드웨어 자원을 사용할 수 있다.

게스트os는 호스트os에 시스템콜을 보내서 하드웨어 자원을 사용하는데 
이 때 하이퍼 바이저 소프트웨어가 언어를 번역해줌