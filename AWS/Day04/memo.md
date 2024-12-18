Ram - 휘발성 - Random access memory
Rom - 비휘발성 Read only memory

why do we need Storage
데이터보존
정보접근성
비즈니스 연속성 , 백업 및 복구
법정 규정 준수
app 운영

snapshot - 백업 본

EBS - elastic block storage
DAS 연결형식

EFS - elastic File storage
nas 연결 

NFS -network file system

sg chaining 
- sg로 인바운드 된 트래픽 허용

encrypt??


Database
₩체계적₩으로 구성되어 쉽게 접근, 관리, 업데이트 할 수 있는 데이터의 집합

주요 유형 
관계형 데이터베이스 : sql기반 테이블 구조 

가장 중요한 4가지 개념
integrity 무결성
데이터의 정확성, 일관성, 유효성
개체 무결성 Entity integrety 
모든 테이블이 기본키를 가져야 함 

참조 무결성 referntial integrity 
참조 관계에 있는 두 테이블의 데이터가 항상 일관된 값을 갖는다

도메인 무결성 domain integrity
제약조건으로 도메인 무결성을 보장할 수 있음

acid - 원자성 일관성 격리성 지속성
atomicity 트랜잭션의 모든연산이 완전히 수행되거나 전혀 수행되지 않아야 함
consistency 트랜잭션 신행 전후로 데이터베이스가 일관된 상태를 유지해야함
isolation 동시에 실행되는 트랜잭션들이 서로 영향을 미치지 않아야 함
durability 성공적으로 완료된 트랜잭션의 결과는 영구적으로 반영되어야 함
crud

schema
개념 스키마 - 논리적 스키마, 제약조건, 

내부스키마 - 물리적인 저장장치 위에 어떻게 정의할 것인지

외부스키마 - 실제 데이터들을 형식이나 구조, 화면을 통해 사용자에게 제공 전체 디비의 논리적인 부분

erd 중요 

nosql 
비관계형, 분산, 수평적 확장이 용이한 데이터 베이스 시스템
유연한 스키마를 가진 대량의 데이터 처리에 적합

수평적 확장성 
고가용성
대용량 데이터 처리

무결성 보장 
BASE
basically available -
soft-state
eventually Consistency 

aws - rds 사용 
클라우드에서 관계형 데이터베이스를 쉽게 설정
지원 db
mysql, postgre, maria, oracle, microsoft sql server

주요 특징
자동화된 패치 및 마이너 버전 업그레이드
백업 및 복원 기능
모니터링 및 지표 


nosql -dynamodb
키-값 및 문서 데이터 모델을 지원하는 서버리스 

serverless
아마존에서 직접 관리하는 서비스
