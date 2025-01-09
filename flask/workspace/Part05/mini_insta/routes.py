from flask import request, Blueprint,jsonify
from models import get_users_list, add_user, get_post,add_post, press_like,delete_user

user_bp = Blueprint('users',__name__, url_prefix='/users')
post_bp = Blueprint('posts',__name__,url_prefix='/users/post')

@user_bp.route('/')
def user_list():
    users = get_users_list()
    return jsonify(users=users),200

@user_bp.route('/', methods=["POST"])
def create_user():
    data = request.get_json()
    username = data.get('username')
    isrun = add_user(username)
    if isrun:
        return jsonify({"username":username}),201
    else:
        return jsonify({"msg":"Invalid name"}),404

@user_bp.route('/<username>', methods=['DELETE'])
def del_user(username):
    a= delete_user(username)
    if a:
        return a
    else:
        return a
    
@post_bp.route('/<username>', methods=['GET','POST'])
def posts(username):
    if request.method == 'GET':
        posts_list = get_post(username)
        if posts_list:
            return jsonify([{"title":post['title'],"likes":post['likes']} for post in posts_list]),200
        else:
            return {'msg':'any posts not exist'}
    if request.method =='POST':
        new_data = request.get_json()
        title = new_data.get('title')
        new_post = add_post(username, title)
        if new_post:
            return jsonify(title=new_post),201
        else:
            return jsonify('failed post upload')

@post_bp.route('/like/<username>/<title>',methods=["PUT"])
def like_it(username,title):
    post = press_like(username, title)
    if post:
        return jsonify({"title":post['title'],"likes":post['likes']})
    else:
        return jsonify('failed post upload'),404

