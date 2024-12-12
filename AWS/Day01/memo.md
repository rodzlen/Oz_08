# Infra 
- 서비스 : 4개의 레이어로 돌아감 
- infrastructure 맥북, 서버, 
- Data 코드를 위한 데이터
- Application 코드
- Platform 맥 OS, Flask

## infrasructure
기반임
- hardware
  - 서버장비
  - 스토리지
  - 네트워크
- software
- network
  - OSI 7계층
    - app7 - 평문 단계 아래로 내려갈 때 캡슐화를 거쳐 압축됨 (http)
    - presentation 6
    - session
    - transport - 전송방식 TCP/UDP 어떻게 주고받는지 
    - network - 인터넷 라우팅 ( 어떤 경로로 찾아가는지 주소)
    - datalink - 내부통신 (컴퓨터 두대에서 필요한 정보를 담는) mac 주소
    - physcal - 전기신호
- security

-----
protocol - 통신 약속

tcp/ip 프로토콜 - 4계층 

capsulation -
    - 7 -> 데이타 
    - 5 -> 세그먼트 + 데이타
    - 3 -> 패킷 + 5
    - 2 -> 프레임 + 3
IP = 인터넷에서 사용하는 고유 주소 
123.123.123.1
class, Aclass , bclass cclass 한 자리 최대는 255 - 2^8
약속 ip protocol
public ip - private ip가 아닌 모든 ip
private ip - RFC1918약속  10.0.0.0 부터 10.255.255.255
                            172.16.0.0 172.31.255.255
                            192.168.0.0 - 192.168.255.255
                            class 단위로 주소를 준다 .
                            ip의 낭비를 줄이기 위해 cidr - 고정될 자리수 (앞에서부터 고정 )
                            c class 까지 고정이라고 하면 10.0.0.0/24
                            10.0.1.0 부터 10.0.1.64 까지면 10.0.1.0/26 사용개수 구하면 총 비트 32 에서 26 뺀 수를 2의 n승
UDP user dategram protocol
tcp  transmission 
    연결기반 통신, 신뢰할 수 있는 통신 - 유실데이터가 없어서

    s- c 구조 
    3 hand shaking 방식 

    1 syncronization - syn 
    클라 -> 서버

    2 acknowlege - ack +
        syn
    서버 -> 클라

    3 ack
    클라 -> 서버

중간 과정 

4 hand shaking 

fin 

ack 
fin 

ack

끝 맺음이 다른 이유 데이터 