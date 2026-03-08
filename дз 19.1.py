from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'hello'

@app.route('/about')
def about():
    return 'hi my name is --- i am --- years old , its nice to meet ya'

@app.route('/skills')
def skills():
    return 'i have the following skills: ---, ---, ---'

@app.route('/contact')
def contact():
    return 'u can concant me via attached contanct details , --- , --- or ---'

app.run()