# API CRUD
from flask import request, jsonify
from flask_smorest import abort, Blueprint

def create_posts_blueprint(mysql):
    posts_blp = Blueprint('posts', __name__, description = 'Operatino blog', url_prefix="/posts")

    @posts_blp.route('/',methods=['GET','POST'])
    def posts():
        cursor = mysql.connection.cursor()
        if request.method == 'GET':
            sql = "SELECT * FROM POSTS"
            cursor.execute(sql)
            posts = cursor.fetchall()
            cursor.close()

            posts_list = []
            for post in posts:
                posts_list.append({
                    'id':post[0],
                    'title':post[1],
                    'content':post[2]
                })

            return jsonify(posts_list)
        
        if request.method == 'POST':
            title = request.json.get('title')
            content = request.json.get('content')

            if not title or not content:
                abort(40, message="Title or Content cannot be empty")
            
            sql = f"INSERT INTO posts(title,content) VALUES(%s,%s)"
            cursor.execute(sql,(title,content))
            mysql.connection.commit()

            return jsonify({"msg":"successfully create data"}),201
    
    @posts_blp.route('/<int:post_id>', methods=['GET','PUT','DELETE'])
    def post(post_id):
        cursor = mysql.connection.cursor()
        if request.method == 'GET':
            sql = f"SELECT * FROM posts WHERE id ='{post_id}'"
            cursor.execute(sql)
            post_data = cursor.fetchone()

            if not post_data:
                abort(404, message='Not found data')
            return jsonify({'id':post_data[0],'title':post_data[1],'content':post_data[2]})


        elif request.method =="PUT":
            title = request.json.get('title')
            content = request.json.get('content')
            if not title or not content:
                abort(400, 'Not found title, content')
            sql = "UPDATE posts SET title=%s, content=%s WHERE id = %s"
            
            cursor.execute(sql,(title, content,post_id))
            mysql.connection.commit()

            return jsonify({"msg":"successfully update content"}),200

        elif request.method == "DELETE":
            
            sql = f"DELETE FROM psots WHERE id='{post_id}'"
            cursor.execute(sql)
            mysql.connection.commit()

            return jsonify({"msg": "Successfully deleted "})
    
    return posts_blp

