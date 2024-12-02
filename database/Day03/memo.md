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
- 조건 조회 
  - WHERE : SELECT * FROM 테이블명 WHERE 컬럼명 = x 
  - BETWEEN AND : SELECT * FROM 테이블명 WHERE 컬럼명 BETWEEN x and y; 컬럼명의 x와 y 사이의 값을 가진 데이터 조회 
  - LIMIT : 전체 데이터 중 상위 몇개만 보이게 혹은 페이징 
    - SELECT * FROM 테이블명 LIMIT 10, 5; 10번쨰 부터 5개 조회 ** 페이지네이션, 페이징
  - GROUP BY 
    - SELECT age, COUNT(*) as user_count FROM users GROUP BY age; 각각에 나이에 대한 갯수를 조회
  - CASE WHEN
    - SELECT username, age, CASE WHEN age>=30 THEN '성인' ELSE '미성년자' END  AS age_group FROM users;
      - age의 값이 30 이상이면 성인, 아니면 미성년자인 레코드를 age_group으로 띄운다
  - JOIN
    - SELECT users.name, users.age, orders.order_id FROM users JOIN orders ON users.user_id = orders.user_id;
      - users 테이블의 해당 열값을 표시하는데 orders 테이블의 user_id와 users 테이블의 user_id가 같은 값을 찾아서 띄움
  - ROW_NUMBER() 
    - SELECT username, age FROM users ROW_NUMBER() OVER (ORDER BY age DESC) AS rank FROM users;
      - username, age를 age 내림차순을 부여한 rank열에 조회
### UPDATE
- UPDATE SET 
  - UPDATE 테이블 명 SET 컬럼1 = 값, 컬럼2 = 값 WHERE 조건;
### DELETE 
- DELETE FROM users WHERE username = '김휘수';
- DELETE FROM users WHERE age =25 LIMIT;
- DELETE FROM users AS u JOIN orders AS o ON u.id = o.id WHERE u.username = 유저 테이블과 오더 테이블에서 id 가 같고 김이라는 이름을 가진 사람의 데이터를 삭제
- DELETE FROM employees USING employees AS e, departments AS d WHERE e.departments_id = d.id AND d.name = 'HR';

### JOIN
- INNER JOIN (내부조인) 테이블 A를 기준으로 테이블 B를 합하여 생성
```mysql
-- 기본구조
-- 테이블 A를 기준으로 A의 키값과 매칭되는 B의 키값을 합쳐서 조회
selct * from table A
left join table B
on A.key = B.key
```

**enum(x,y)**: enum()안에 포함된 값 중에서만 생성할 수 있다.
