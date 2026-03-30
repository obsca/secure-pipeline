# app/vulnerable_app.py
import sqlite3
from flask import Flask, request

app = Flask(__name__)

conn = sqlite3.connect('test.db', check_same_thread=False)
c = conn.cursor()
c.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)')

@app.route('/login')
def login():
    username = request.args.get('username')
    password = request.args.get('password')

    # Уязвимость: SQL injection
    #query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    c.execute(query)
    user = c.fetchone()

    if user:
        return f"Welcome {username}"
    else:
        return "Login failed"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
