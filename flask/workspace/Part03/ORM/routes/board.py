from flask import request, jsonify
from flask_smorest import Blueprint
from flask.views import MethodView
from db import db
from models import Board

board_blp = Blueprint('Boards', 'boards', description='Operations on boards', url_prefix='/board')

# API List
# /board/
# 전체 게시글을 가져오는 API (get)
@board_blp.route('/')
class BoardList(MethodView):
    def get(self):
        boards = Board.query.all()
        for board in boards:
            print('id',board.id)
            print('title',board.title)
            print('content',board.content)
            print('author_email',board.author.email) # join 쿼리가 한줄에? ㅋ
        
        print(boards)
        return jsonify([{'id': board.id, 'title':board.title, 'content': board.content, 'author_name':board.author.id}for board in boards ])
    def post(self):
        data = request.json
        new_borad = Board( title= data['title'], content=data['content'], user_id= data['user_id'])
        db.session.add(new_borad)
        db.session.commit()
        return jsonify({'msg':'succes created board'}),201
# 게시글을 작성하는 API (post)

#/board/<int:board_id>
# 하나의 게시글 불러오기 (get)
@board_blp.route('/<int:board_id>')
class BoardResource(MethodView):
    def get(self,board_id):
        board = Board.query.get_or_404(board_id)

        return jsonify({'title':board.title,
                        'id': board.id,
                        'content': board.content,
                        'author': board.author.name})
# 특정 게시글 수정(put)
    def put(self, board_id):
        board = Board.query.get_or_404(board_id)
        data = request.json
        board.title = data['title']
        board.content = data['content']
        db.session.commit()
        
        return jsonify({"msg":"successfully updated board data"}), 201

# 특정 게시글 삭제(delete)
    def delete(self,board_id):
        board = Board.query.get_or_404(board_id)
        if board:
            db.session.delete(board)
            db.session.commit()

            return jsonify({"msg":"successfully data"}),204
        
        else: 
            return jsonify({"msg":"not found data"}),404


