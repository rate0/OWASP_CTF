from flask import Flask, request, render_template, redirect, url_for, session
import hashlib
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

users = {
    "admin": "5ebe2294ecd0e0f08eab7690d2a6ee69"  
}

FLAG = os.getenv('FLAG', 'FLAG_NOT_SET')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = hashlib.md5(password.encode()).hexdigest()
        if username in users and users[username] == hashed_password:
            session['username'] = username
            return redirect(url_for('flag'))
        else:
            return render_template('login.html', error="Invalid credentials")
    return render_template('login.html')

@app.route('/flag')
def flag():
    if 'username' in session:
        return render_template('flag.html', flag=FLAG)
    else:
        return redirect(url_for('login'))

@app.route('/source')
def source():
    code = ''
    with open(__file__, 'r') as f:
        code = f.read()
    return render_template('source.html', code=code)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
