from flask import Flask, render_template, request, redirect, url_for, session, flash, make_response
import sqlite3
import base64
import atexit

app = Flask(__name__)
app.secret_key = 'secret_key_here'

DATABASE = 'users.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def encode_role(role):
    return base64.b64encode(role.encode()).decode()

def decode_role(encoded_role):
    return base64.b64decode(encoded_role.encode()).decode()

@app.route('/')
def index():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    else:
        return redirect(url_for('profile'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password)).fetchone()
        conn.close()
        if user:
            session['logged_in'] = True
            session['username'] = user['username']
            encoded_role = encode_role(user['role'])
            response = make_response(redirect(url_for('profile')))
            response.set_cookie('role', encoded_role)
            flash('Вы вошли!')
            return response
        else:
            flash('Неверное имя или пароль')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        role = 'user'  # Задаем роль по умолчанию
        conn = get_db_connection()
        try:
            conn.execute('INSERT INTO users (username, password, role) VALUES (?, ?, ?)', (username, password, role))
            conn.commit()
        except sqlite3.IntegrityError:
            flash('Username already exists.')
            return redirect(url_for('register'))
        finally:
            conn.close()
        
        # Автоматический вход после регистрации
        session['logged_in'] = True
        session['username'] = username
        encoded_role = encode_role(role)  # Кодируем роль в base64
        response = make_response(redirect(url_for('profile')))
        response.set_cookie('role', encoded_role)  # Сохраняем роль в куки
        flash('Registration successful. You are now logged in.')
        return response
    return render_template('register.html')


@app.route('/profile')
def profile():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    encoded_role = request.cookies.get('role', encode_role('user'))
    role = decode_role(encoded_role)
    if role == 'admin':
        flag = 'IR{BAC_i5_3z_wh3n_y0u_4r3_4dm1n}'
    else:
        flag = 'Нет доступа'
    return render_template('profile.html', username=session['username'], role=role, flag=flag)

@app.route('/logout')
def logout():
    session.clear()
    response = make_response(redirect(url_for('index')))
    response.set_cookie('role', '', expires=0)
    flash('Вы вышли из аккаунта.')
    return response

def clear_db():
    with sqlite3.connect(DATABASE) as conn:
        conn.execute('DELETE FROM users')
        conn.commit()
    print('База данных пользователей очищена.')

atexit.register(clear_db)

if __name__ == '__main__':
    app.run(debug=True)
