import sqlite3

DATABASE = 'users.db'

def init_db():
    conn = sqlite3.connect(DATABASE)
    conn.execute('''CREATE TABLE users
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 username TEXT UNIQUE NOT NULL,
                 password TEXT NOT NULL,
                 role TEXT NOT NULL)''')
    conn.execute("INSERT INTO users (username, password, role) VALUES ('admin', 'super_strong_admin_p@ssw0rd', 'admin')")
    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()
