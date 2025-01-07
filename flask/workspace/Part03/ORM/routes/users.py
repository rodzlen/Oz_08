from flask import request, jsonify
from flask_smorest import Blueprint
from db import db
from models import User
from flask.views import MethodView

user_blp = Blueprint('Users','users', description= 'Operation user data', url_prefix='/users')

@user_blp.route('/')
class UserList(MethodView):
    def get(self):
        users = User.query.all()
        
        return jsonify([{"id":user.id, "name":user.name, "email":user.email} for user in users])
    
    def post(self):
        data = request.json
        new_user = User(name=data['name'],email=data['email'])
        db.session.add(new_user)
        db.session.commit()

        return jsonify({"msg":"successfully added data"}),201
    
@user_blp.route('/<int:user_id>')
class UserResource(MethodView):
    def get(self, user_id):
        user = User.query.get_or_404(user_id)
        
        return jsonify({"id":user.id,"name":user.name,"email":user.email}), 200

    def put(self, user_id):
        data = request.json
        user = User.query.get_or_404(user_id)
        user.name = data['name']
        user.email = data['email']
        db.session.commit()
        
        return jsonify({"msg":"successfully update data"}),200
    
    def delete(self, user_id):
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        
        return jsonify({'msg':"successfully deleted data"}), 200
        