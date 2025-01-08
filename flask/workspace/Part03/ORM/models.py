# Model은 Table 생성 
# board (모델은 하나니까 단수임)
# user

from db import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable =False)
    email = db.Column(db.String(100), unique=True, nullable = False)
    address = db.Column(db.String(200), nullable= False)
    boards = db.relationship('Board', back_populates ='author', lazy='dynamic') # workbench에서는 보이지 않음 관계를 그냥 정의했을 뿐임

class Board(db.Model):
    __tablename__ = 'boards'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100),nullable=False)
    content = db.Column(db.String(300))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    author = db.relationship('User', back_populates = 'boards')

