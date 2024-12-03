import pymysql
import pymysql.cursors
# db.connection
connection = pymysql.connect(
    host= "localhost",
    user='root',
    password='1234',
    db='classicmodels',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor     # 결과값이 dict형태로 반환, 기본은 튜플
)
cursor = connection.cursor()

# select
def get_customers():
    sql = 'select * from customers'
    cursor.execute(sql)
    customers = cursor.fetchone() # 하나의 정보만 가져올 때는 fetchone()

    print(customers)
    print("customers : ",customers['customerName'])
    cursor.close()

# insert into
def insert_customer():
    cursor = connection.cursor()
    name = '휘수'
    family_name = '김'
    sql = f'insert into customers(key, key2) values("{name}","{family_name}")'
    cursor.execute(sql)
    connection.commit() # 쿼리문 실행 후 데이터베이스에 반영하는 코드 
    cursor.close()
# update
def update_customer():
    cursor = connection.cursor()

    update_name= '김휘수'
    sql = f"update customers set customerName='{update_name}' where customerNumber = 103"
    cursor.execute(sql)
    connection.commit()
    cursor.close()

# delete
def delete_customer():
    cursor = connection.cursor()
    sql = "delete from customers where customerNumber = 103"
    cursor.execute(sql)
    connection.commit()
    cursor.close()
delete_customer()