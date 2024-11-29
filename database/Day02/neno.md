# day02 
## SQL (Strucktured Query Language)
- SQL은 관계형 데이터베이스에서 데이터를 정의, 처리, 제어 하는데 사용되는 표준화된 언어.
- SQL은 DBMS와 상호작용을 위해 설계되었다.

### 데이터 정의 언어(Data Define Lanuage)
- DDL은 데이터베이스의 구조를 정의하는데 사용됩니다.
    - CREAATE: 데이터베이스의 객체를 생성 
    - ALTER: 데이터베이스의 객체를 수정
    - DROP: 데이터베이스의 객체를 삭제
    - TRUNCATE: 테이블의 모든 레코드(행)를 삭제하지만 테이블은 유지
### 데이터 처리 언어(Data Mainpulation Language)
- DML은 데이터를 검색, 삽압, 수정, 삭제하는데 사용 
  - SELECT: 데이터베이스에서 정보를 검색
  - INSERT: 새로운 데이터를 테이블에 삽입
  - UPDATE: 테이블의 기존 데이터를 수정
  - DELETE: 테이블에서 데이터를 삭제

### 데이터 제어 언어 (Data Control Language)
- DCL은 데이터베이스에 대한 엑세스를 제어하는데 사용
    - GRANT: 사용자에게 특정 작업을 수행할 권한을 부여
    - REVOKE: 사용자로부터 특정 작업 수행 권한을 제거