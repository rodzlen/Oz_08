from flask import Flask, render_template, request, redirect, session, flash
from datetime import timedelta

app = Flask(__name__)

app.secret_key = 'flask-secret-key'
app.config['PERMANENT_SESSION_LIFETIME']= timedelta(days=7)
users = {
    'sohn':'pw123',
    'leo': 'pw123'
}

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login',methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username in users and users[username] == password:
        session['username']= username
        session.permanent = True
        return redirect('/secret')
    else: 
        flash("Invaild username or password")
        return redirect('/')

@app.route('/secret')
def secret():
    if 'username' in session:
        return render_template('secret.html')
    else:
        return redirect('/')
    
# 로그아웃 구현
@app.route('/logout')
def logout():
    session.pop('username', None)
    session.clear()
    return redirect('/')

if __name__ =="__main__":
    app.run(debug=True)