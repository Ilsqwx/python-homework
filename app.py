from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():

    conn = sqlite3.connect("events.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS events (
        id INTEGER PRIMARY KEY,
        name TEXT,
        date TEXT,
        time TEXT,
        priority TEXT
    )
    """)

    if request.method == "POST":

        if "add" in request.form:

            name = request.form["name"]
            date = request.form["date"]
            time = request.form["time"]
            priority = request.form["priority"]

            cursor.execute(
                "INSERT INTO events (name, date, time, priority) VALUES (?, ?, ?, ?)",
                (name, date, time, priority)
            )

        if "delete" in request.form:

            i = int(request.form["delete"])

            cursor.execute("SELECT id FROM events")
            ids = cursor.fetchall()

            if i < len(ids):

                event_id = ids[i][0]

                cursor.execute(
                    "DELETE FROM events WHERE id = ?",
                    (event_id,)
                )

    conn.commit()

    cursor.execute("SELECT name, date, time, priority FROM events")
    rows = cursor.fetchall()

    events = []

    for r in rows:
        events.append(r[0] + " | " + r[1] + " | " + r[2] + " | " + r[3])

    conn.close()

    return render_template("index.html", events=events)


app.run(debug=True)