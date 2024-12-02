# Day03
## DML
  제약조건에 따른 INSERT방법
  - ON DUPLICATE KEY UPDATE(설정할 키 값)
    - 입력하는 키 값 중 중복제약 조건에 걸리는 경우 필드에 설정하는 기능
  - INSERT IGNORE INTO ()
    - 중복 제약 조건에 위배되면 INSERT 명령을 무시한다
  - REPLACE INTO ()
    - 중복 제약조건에 위배되면 해당 레코드를 삭제하고 다시 삽입한다.
  - SET 절을 이용한 INSERT
  - INSERT INTO users SET username='홍길동', email='asd@asd.com', age = 24 이런식으로 작성 

### SELECT 
- 중복 데이터 제외하고 조회 
  - DISTINCT : SELECT DISTINCT 컬럼명 FROM 테이블명 
- 데이터 정렬
  - ORDER BY: SELECT 컬럼명 FROM 테이블명 ORDER BY x ASC, y DESC -- x는 오름차순으로 y는 내림차순으로 