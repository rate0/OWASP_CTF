import hashlib
from flask import render_template, request, redirect, url_for, flash, session
from app import app

# Ожидаемый MD5 хэш для строки "hello"
EXPECTED_HASH = "5d41402abc4b2a76b9719d911017c592"

# Главная страница
@app.route('/')
def index():
    return render_template('index.html')

# Страница загрузки файлов
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            file_content = file.stream.read()
            file_hash = hashlib.md5(file_content).hexdigest()
            
            # Сравнение хэша загруженного файла с ожидаемым
            if file_hash == EXPECTED_HASH:
                # Сохраняем состояние в сессии, что файл был загружен правильно
                session['flag_access_granted'] = True
                return redirect(url_for('flag'))
            else:
                flash('File integrity check failed!', 'error')
    return render_template('upload.html')

# Страница с флагом
@app.route('/flag')
def flag():
    # Проверяем, есть ли доступ к странице с флагом
    if session.get('flag_access_granted'):
        return render_template('flag.html', flag="IR{5of7w4r3_1n73gr1ty_f41lur3}")
    else:
        abort(403)  # Ошибка доступа

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
