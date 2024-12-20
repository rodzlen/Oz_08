aws
글로벌 인프라 
- Rezion 3개 이상의 AZ
- 가용영역 AZ
- edge location
- 하나 이상의 데이터센터 aws 네트워크로 묶어놈
- api rest ****** http 
- sdk 개발용 python은 boto3

internet 기반 
- 보안을 위해 vpc 사용 
- 외부에 있는 서버와 통신하기 위해 VPC Endpoint를 사용 (internet 사용 안함)
- 리전간 통신을 위한 서비스 - vpc peering 
- RT 에 igw 규칙을 정해주어야 함 10.0.0.0 ~ 
- multi az - 고가용성 
- elb 가 도메인 만들어서 endpoint 제공 
nacl - 서브넷단위로 보안을 줌 
sg - ec2 단위로 보안 들어오는것 기본적으로 차단 inbound 설정 해줘야 함 
ami - amazon machine image
Auto Scailing Group - 설정한 범위 내에서 수평적 확장

arn 읽을줄 알아야 
lambda - 단위 function runtime 까지 만들어 제공  vpc 만들필요 없음, 메모리 크기에 따라 비례적으로 정함 
api gateway -rest api 
route 53  - dns 포트번호 

cash 서버 

role ***** 
인증 만료기간이 있는 역할 부여 
리소스에 권한을 주어야 함 
execution role