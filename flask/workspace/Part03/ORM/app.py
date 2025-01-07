from flask import Flask
from flask_smorest import Api
from db import db
from models import User, Board

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1234@localhost/oz'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =False # 트래킹 계속 할건지 -> 부하가 크기 때문에 false로 보통 설정

db.init_app(app)

# blp 설정

app.config["API_TITLE"] = "My API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.1.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)
#api.register_blueprint()

from flask import render_template

@app.route('/manage-boards')
def manage_boards():
    return render_template('board.html')

@app.route('/manage-users')
def manage_users():
    return render_template('users.html')

from routes.board import board_blp
from routes.users import user_blp
app.register_blueprint(board_blp)
app.register_blueprint(user_blp)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)