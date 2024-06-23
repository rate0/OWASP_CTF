from flask import Flask, render_template, request, redirect, url_for, flash, session
import logging
import os
import base64

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Configure logging
logging.basicConfig(filename='logs/all_logs.log', level=logging.INFO, format='%(asctime)s %(message)s')

# Function to read logs from a specified file
def read_logs(log_file):
    logs_content = ''
    if os.path.exists(log_file):
        with open(log_file, 'r') as file:
            logs_content = file.read()
    return logs_content

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    # Log the login attempt
    app.logger.info(f"Login attempt with username: {username} and password: {password}")
    
    if username == 'admin' and password == 'P@ssw0rd!23':
        session['admin'] = True
        flash("Welcome admin!", 'success')
        return redirect(url_for('admin'))
    else:
        flash("Invalid credentials", 'danger')
        return redirect(url_for('index'))

@app.route('/logs', methods=['GET'])
def logs():
    # Log user access to /logs directory
    app.logger.info("User accessed the /logs directory.")
    
    # Read all logs from the combined log file
    log_file = 'logs/all_logs.log'
    logs_content = read_logs(log_file)
    
    # Render logs.html template with log content
    return render_template('logs.html', logs_content=logs_content)

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/secret_logs', methods=['GET'])
def secret_logs():
    # Check if admin is authenticated
    if 'admin' not in session or not session['admin']:
        flash("You need to login as admin to view secret logs.", 'danger')
        return redirect(url_for('index'))
    
    # Log admin access to /secret_logs
    app.logger.info("Admin accessed the /secret_logs directory.")
    
    # Simulate secret actions in secret_logs
    secret_logs_content = "Performed secret action 1.\nPerformed secret action 2.\nCreated file \"flag.txt\": SVJ7bG9nZzFuOV8xNV9teV9sMWYzfQ=="
    return render_template('secret_logs.html', secret_logs_content=secret_logs_content)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1000)
