from flask import Flask,request, render_template, redirect

app = Flask(__name__)

users = [
    {"username": "traveler", "name": "Alex"},
    {"username": "photographer", "name": "Sam"},
    {"username": "gourmet", "name": "Chris"}
]

@app.route('/')
def index():    
    return render_template('index.html', users = users)

@app.route('/add',methods=['GET','POST'])
def add_user():
    if request.method == 'GET':

        return render_template('add_user.html')
    
    if request.method == 'POST':
        username = request.form['username']
        name = request.form['name']
        users.append({"username":username,"name":name})

        return redirect('/')
    
@app.route('/edit/<string:username>', methods=['GET','POST'])
def edit(username):
    if request.method == 'GET':
        user = []
        for i in users:
            if i['username'] == username:
                user.append(i)
                break
            
        return render_template('edit_user.html', user = user)


    if request.method == 'POST':
        new_name = request.form['name']
        for user in users:
            if user['username'] == username:
                user['name']= new_name
                return redirect('/')
            
@app.route('/delete/<string:username>')
def delete_user(username):
    for i in users:
        if i['username'] == username:
            users.remove(i)
            return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
            