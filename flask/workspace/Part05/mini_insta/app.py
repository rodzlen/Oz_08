from flask import Flask
from routes import user_bp,post_bp

app = Flask(__name__)
app.register_blueprint(user_bp)
app.register_blueprint(post_bp)


if __name__ == "__main__":
    app.run(debug=True)