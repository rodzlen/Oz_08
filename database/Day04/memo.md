# Day04
데이터베이스 연동

## pymysql을 이용한 데이터베이스 연동
커넥션 설정 
```python
connection = pymysql.connect(
    host = "localhost" # ip주소
    user = 'root' # 데이터베이스 유저 이름
    password = '1234'  # 데이터베이스 패스워드
    db = 'classicmodels' # 데이터베이스 이름
    charset = 'utf9mb4' # 인코딩 설정
    cursorclass = pymysql.cursors.Dictcursor # 반환 형식 설정 기본은 튜플
)

cursor = connection.cursor()

sql = 'select * from customers' # sql문 생성
cursor.excute(sql) # 쿼리 날리기

customers = cursor.fetchone() # 날린 쿼리문에서 하나의 정보만 가져오기 
 ```
 
 - `cursorclass`
   - Default Cursor(`pymysql.cursors.Cursor`) : 기본 커서 클래스로 각 행을 튜플 형식으로 반환 열 이름 정보는 포함하지 않음
   - DictCursor(`pymysql.cursors.Dictcursor`) : 결과를 딕셔너리로 반환
   - SSCursor(`pymysql.cursors.SSCursor`) : 서버사이드 커서로 큰 결과 집합을 처리할 떄 유용 모든 결과를 한 번에 메모리에 로드하지 않고 필요할 때마다 서버에서 행을 가져옴
   - SSDictCursor(`pymysql.cursors.SSDictCursor`) : 위의 내용을 딕셔너리로 반환