from flask import Flask, render_template, request, redirect
import sqlite3
from datetime import datetime

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            created_at TEXT
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/author")
def author():
    return render_template("author.html")

@app.route("/planner")
def planner():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM tasks")
    tasks = c.fetchall()
    conn.close()

    return render_template("planner.html", tasks=tasks)

@app.route("/add_task", methods=["POST"])
def add_task():
    title = request.form["task"]
    description = request.form["description"]
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute(
        "INSERT INTO tasks (title, description, created_at) VALUES (?, ?, ?)",
        (title, description, created_at)
    )
    conn.commit()
    conn.close()

    return redirect("/planner")

@app.route("/delete/<int:id>")
def delete(id):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("DELETE FROM tasks WHERE id = ?", (id,))
    conn.commit()
    conn.close()

    return redirect("/planner")

if __name__ == "__main__":
    app.run(debug=True)