from flask import Flask, request, render_template, redirect, url_for, flash
import os
import hashlib
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timedelta

app = Flask(__name__)
app.secret_key = 'supersecretkey'
FLAG = "IR{5of7w4r3_1n73gr1ty_f41lur3}"
UPLOAD_FOLDER = 'uploads'
DELETE_AFTER_SECONDS = 300  # Time in seconds after which the file will be deleted (e.g., 300 seconds = 5 minutes)

scheduler = BackgroundScheduler()
scheduler.start()

def save_file(file):
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)
    schedule_file_deletion(file_path)
    return file_path

def schedule_file_deletion(file_path):
    delete_time = datetime.now() + timedelta(seconds=DELETE_AFTER_SECONDS)
    scheduler.add_job(delete_file, 'date', run_date=delete_time, args=[file_path])

def delete_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"File {file_path} deleted.")

def is_file_integrity_compromised(file_path):
    expected_hash = "5d41402abc4b2a76b9719d911017c592"  # MD5 hash of "hello"
    with open(file_path, "rb") as f:
        file_hash = hashlib.md5(f.read()).hexdigest()
    return file_hash != expected_hash

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file:
            file_path = save_file(file)
            if is_file_integrity_compromised(file_path):
                os.remove(file_path)
                flash('File integrity check failed!')
                return redirect(request.url)
            else:
                flash(f"File uploaded successfully! Here is your flag: {FLAG}")
                return redirect(request.url)
    return render_template('upload.html')

if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(host='0.0.0.0', port=9000)
