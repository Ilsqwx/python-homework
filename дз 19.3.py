from flask import Flask

app = Flask(__name__)

@app.route('/math/<operation>/<int:a>/<int:b>')
def math(operation, a, b):

    if operation == "add":
        return str(a + b)

    elif operation == "sub":
        return str(a - b)

    elif operation == "mul":
        return str(a * b)

    elif operation == "div":
        if b == 0:
            return "Error: division by zero"
        return str(a / b)

    else:
        return "Invalid operation"


if __name__ == "__main__":
    app.run()