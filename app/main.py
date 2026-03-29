from fastapi import FastAPI
import sqlite3

app = FastAPI()

@app.get("/users")
def get_user(name: str):
    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()

    # ❌ SQL injection для демонстрации
    cursor.execute("SELECT * FROM users WHERE name = ?", (name,))
    cursor.execute(query)

    return {"data": cursor.fetchall()}
