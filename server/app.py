from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:text>')
def print_string(text):
    print(text)  # Console output
    return text  # Plain text response (no HTML)

@app.route('/count/<int:number>')
def count(number):
    # Generate numbers 0 to number - 1 on separate lines
    return '\n'.join(str(i) for i in range(number)) + '\n'

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        return str(num1 + num2)
    elif operation == '-':
        return str(num1 - num2)
    elif operation == '*':
        return str(num1 * num2)
    elif operation == 'div':
        return str(num1 / num2)
    elif operation == '%':
        return str(num1 % num2)
    else:
        return 'Invalid operation', 400  # Bad request

if __name__ == '__main__':
    app.run(port=5555, debug=True)
