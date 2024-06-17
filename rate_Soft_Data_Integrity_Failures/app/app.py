from flask import Flask, render_template, request, send_from_directory, redirect, url_for, flash, abort
import os
import time
import threading
from werkzeug.utils import secure_filename
from utils import process_update, cleanup_old_files

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['ALLOWED_EXTENSIONS'] = {'zip', 'tar', 'gz'}

# Путь к файлу с флагом
FLAG_FILE = 'flags/flag.txt'
ADMIN_SECRET_KEY = 'admin_secret_key'

# Функция для проверки разрешенных расширений файлов
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/admin')
def admin():
    # Скрытый комментарий для намека на уязвимость
    hidden_comment = "<!-- HINT: Pay attention to how filenames are processed. -->"
    return render_template('admin.html', hidden_comment=hidden_comment)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        # ВНИМАНИЕ: Уязвимость - небезопасная обработка имени файла
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        process_update(filename)  # Обработка обновления, которая будет уязвима
        return redirect(url_for('index'))
    else:
        flash('Invalid file type')
        return redirect(request.url)

@app.route('/download/<path:filename>', methods=['GET'])
def download(filename):
    try:
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)
    except FileNotFoundError:
        abort(404, 'File not found.')

@app.route('/flag')
def flag():
    # Флаг доступен только для пользователей, которые нашли уязвимость
    secret_key = request.args.get('key')
    if secret_key == ADMIN_SECRET_KEY:
        with open(FLAG_FILE, 'r') as f:
            flag = f.read()
        return flag
    else:
        return 'Access denied.'

if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    # Запуск фоновой задачи для очистки старых файлов
    cleanup_thread = threading.Thread(target=cleanup_old_files, args=(app.config['UPLOAD_FOLDER'],))
    cleanup_thread.daemon = True
    cleanup_thread.start()
    app.run(host='0.0.0.0', port=5000)
