# Day 03 
## ORM 
### SQLAlchemy란?
- 파이썬의 객체 관계 매핑(ORM) 라이브러리 
- SQL이 아닌 ORM 방식으로 DB의 데이터를 조회할 수 있도록 도와줌

### ORM이란?
- Object-Relational Mapping, 문자 그대로 객체와 관계형 데이터베이스 간의 매핑을 의미
- 객체: 파이썬
- 관계: rdbms
- 연결 

이라고 보면 된다 

sql 쿼리문 없이 데이터 crud 가능 

#### 기능
1. Model : DB 테이블 생성을 해주는 역할 
2. ORM : DB 테이블 데이터를 읽어주는 역할 

#### 사용 이유 
- 데이터베이스 관련 코드가 간결해짐
- 결과 오류를 줄일 수 있음 (Schema)
- 쿼리를 쉽게 작성할 수 있음

모델 -> 테이블 만드는
back_populate = 양뱡향으로 연결 서로 참조하는 관계
lazy = 'dynamic'옵션은 많은 수의 관계된 객체들이 있을 때 한번에 다 조회하지 않고 필요한 것만 특정 데이터만 조회할 수 있는 옵션 (쿼리셋) 로딩된건 아니고 반환할 뿐임

sqlalchemy 에서는 db.execute가 아니고 db.session.add() 로 사용 

하나씩 조회 가능
query.filter_by(name='asd').first()

### Model과 Schema의 차이
- Schema: Mashmellow로 스키마를 만들어 데이터 검증을 할 수 있음 데코레리션 형식으로 사용가능 @blueprint.argument(scehma이름) response
- Model : ORM에서 상호작용 하기 위해 필요한 것 (데이터베이스 구조 정의) request
- 