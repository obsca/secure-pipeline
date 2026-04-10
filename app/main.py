#hiii
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
    #c.execute(query)
    #user = c.fetchone()

    if user:
        return f"Welcome {username}"
    else:
        return "Login failed"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
'''

import sqlite3
from flask import Flask, request, jsonify, abort

app = Flask(__name__)

DATABASE = "test.db"


def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/login')
def login():
    username = request.args.get('username')
    password = request.args.get('password')

    # ✅ Валидация входных данных
    if not username or not password:
        abort(400, description="Missing username or password")

    # (опционально) базовая фильтрация длины
    if len(username) > 50 or len(password) > 50:
        abort(400, description="Input too long")

    # ✅ Безопасный запрос (parameterized query)
    try:
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM users WHERE username = ? AND password = ?",
                (username, password)
            )
            user = cursor.fetchone()
    except sqlite3.Error:
        abort(500, description="Database error")

    # ✅ Безопасный ответ (без утечки лишних данных)
    if user:
        return jsonify({"message": f"Welcome {username}"})
    else:
        return jsonify({"message": "Login failed"}), 401


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
