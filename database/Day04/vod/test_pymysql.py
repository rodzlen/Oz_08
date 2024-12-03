import pymysql
import pymysql.cursors
# db.connection
connection = pymysql.connect(
    host= "localhost",
    user='root',
    password='1234',
    db='classicmodels',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor    
)

connection.cursor()

