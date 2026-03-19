from flask import Flask, render_template, request

app = Flask(__name__)

events = []


@app.route("/", methods=["GET", "POST"])
def index():

    global events

    if request.method == "POST":
        if "add" in request.form:

            name = request.form["name"]
            date = request.form["date"]
            time = request.form["time"]
            priority = request.form["priority"]

            text = name + " | " + date + " | " + time + " | " + priority

            events.append(text)
        if "delete" in request.form:

            i = int(request.form["delete"])
            events.pop(i)

    return render_template("index.html", events=events)


app.run(debug=True)