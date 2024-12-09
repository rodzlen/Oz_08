# day08 
## NOSQL 
- MongoDB, Cassandra 
- 대량의 분산된 데이터를 다루거나 동적 스키마, 대용량 및 빠른 속도의 데이터 처리 등을 목표로 하는 다양한 요구 사항에 맞게 설계되었음 분산식으로 저장하기 위해 
- RDBMS 단점
  - 규모 확장성 : 대용량 데이터 처리와 분산 시스템에 대한 지원이 제한적. 수직적 확장에는 잘 잗공하지만, 수평적 확장(서버 증가)에는 비효율적
  - 유연성 부족: 데이터 스키마가 고정되어 있어 변경이나 새로운 데이터 타입의 추가가 어려움 비구조화된 데이터나 변화하는 데이터 구조를 다루는 데에 불편함 초래
  - 복잡한 쿼리 및 트랜잭션 : 대규모 분산 환경에서 전체 조회 쿼리 한번으로 db 뻗을수도

----
## NOsql 데이터 타입
- 정형 데이터 sturctured data 
  - 정해진 스키마에 따라 구조화된 되이터로 관계형 데이터베이스나 스프레드시트, CSV와 같은 형식

- 반정형 데이터 Semi-Structured Data
  - 일정한 구조를 가지고 있지만 데이터 모델에 엄격하게 준수하지 않는 데이터 XML,JSON, HTML, 로그와 같은 형식에서 사용

- 비정형 데이터 Unstructured Data
  - 구조나 형태가 없으며 연산이 어려운 데이터로 영상, 이미지, 음성, 텍스트 등 
  
## MongoDB 
- 문서 기반의 데이터베이스 시스템
- 관계형 데이터베이스의 테이블 대신 JSON/BSON형식의 독적인 문서를 사용

1. 문서 기반 데이터 베이스 
   -  MongoDB는 데이터를 문서 단위로 저장한다. 각 문서는 키 -값 쌍으로 이루어진 BSON 형식으로 표현되고 여러 문서가 컬렉션에 저장된다
2. 유연한 스키마
   -  동적스키마를 사용하며 각 문서가 다른 구조를 가질 수 있다
3. json/bson 형식 

### 구조
- database - collection - document
1. 데이터베이스 :
   -  Mongodb는 여러 개의 데이터베이스를 가질 수 있다. 각 데이터베이스는 독립적으로 관리되고 여러 컬렉션을 포함할 수 있다.
2. 컬렉션 :
   -  컬렉션은 문서의 그룹. 테이블과 유사하게 데이터를 저장하며 스키마가 없어 유연한 구조를 가지고 있다
   -  서로 다른 document들이 하나의 컬렉션에 저장될 수 있다.
3. 문서 :
   -  문서는 MongoDB에서의 기본 데이터 단위로, JSON 형태의 키 - 값 쌍을 갖는다
   -  각 문서는 서로 다른 구조를 가질 수 있으며 필요에 따라 필드를 동적으로 추가할 수 있음
   -  document는 collection 내에 저장되며 각 document는 고유한 objectid를 가진다

## aggregation 
- $match : 데이터 필터링
- $group : 집계화 
- $project : 특정 필드를 선택하거나 새로운 필드를 생성 
- $sort : 결과를 정렬 기본 오름차순
- $limit : 결과의 개수를 제한 
- $skip : 특정 개수의 문서를 건너뜀
- $unwind : 배열 필드를 개별 문서로 분리
- $lookup : 다른 컬렉션과의 조인을 수행 