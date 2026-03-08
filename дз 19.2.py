from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'welcome to the start page'

@app.route('/temperature/<int:i>')
def temp(i):
    if i < 0:
        return 'its cold'
    elif 0 <= i <= 20:
        return 'its pre-cold'
    elif 20 <= i <= 30:
        return 'its warm'
    elif i >= 30:
        return 'its hot'
    else:
        return 'wrong input'

app.run()