from flask import Flask
from flask_mysqldb import MySQL
from flask_smorest import Api

app = Flask(__name__)

# MYSQL 연동 설정 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'oz'

mysql = MySQL(app)

# html 코드로 flask-mysql 테스트
from flask import render_template

@app.route('/user_interface')
def user_interface():
    return render_template("users.html")