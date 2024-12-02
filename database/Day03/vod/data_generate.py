import mysql.connector # 데이터베이스 커넥터 임포트
import random # 내장
from faker import Faker # 더미데이터 라이브러리

# mysql 연결 설정
db_connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='1234', # 문자열로 넣어야함
    database='mydatabase'
)

# mysql 연결
cursor = db_connection.cursor()
fake = Faker()

# # 100개 users 데이터 생성 //먼저 생성 이유는 가장 근본이 되는 데이터이기 때문
# for _ in range(100):
#     username = fake.user_name()
#     email = fake.email()

#     # 데이터 삽입 쿼리문 날리기
#     sql = 'INSERT INTO users (username, email) VALUES(%s,%s)'
#     values = (username,email)
#     cursor.execute(sql, values)

# user_id 불러오기 
cursor.execute('select user_id from users')
valid_user_id = [row[0] for row in cursor.fetchall()]

# 100개의 orders 더미데이터 생성
for _ in range(100):
    user_id = random.choice(valid_user_id) # valid_user_id에서 가져온 값 중에 고른다
    product_name = fake.word() # 더미 단어 생성
    quantity = random.randint(1,10) # 1부터 10 의 랜덤

    try:
        sql = 'insert into orders(user_id, product_name, quantity) values(%s,%s,%s)'
        values = (user_id, product_name, quantity)
        cursor.execute(sql,values)
    except Exception as e:
        print(e)


# commit시켜야 반영이 됨
db_connection.commit()
# 연 순서 차례대로 닫아주기
cursor.close()
db_connection.close()