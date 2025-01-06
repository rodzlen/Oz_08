from flask import Flask, request, Response


app = Flask(__name__)

@app.route('/')
def home():
    return "hello this is main page"

@app.route('/about')
def about():
    return "Hello this is about page"

@app.route('/company')
def company():
    return "Hello this is company page"

@app.route('/number/<int:number>')
def number(number):
    return f'number: {number}'

# 동적으로 URL 파라미터 값을 받아서 처리해줌
@app.route('/user/<username>')
def user_profile(username):
    return f'username: {username}'


# POST 요청을 날리는 법
# postman, reqeusts
import requests
@app.route('/test')
def test():
    url ='http://127.0.0.1:5000/submit'
    data = 'test data'
    
    response = requests.post(url=url, data=data)
    return response
    


@app.route('/submit', methods=['GET', 'POST', 'PUT','DELETE'])
def submit():
    print(request.method)

    if request.method == "GET":
        print("GET method")
    if request.method == 'POST':
        print('POST method', request.data)
    return Response('success' ,status=200)

if __name__ == "__main__":
    app.run()