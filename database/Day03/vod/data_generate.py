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