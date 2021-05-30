from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Hello World :)</h1>'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return "Hello {}".format(name)


@app.route('/<fahrenheit>')
def fahrenheit_to_celsius(fahrenheit):
    celsius = 5 / 9 * (int(fahrenheit) - 32)
    return "Result: {:.2f} c".format(celsius)


if __name__ == '__main__':
    app.run()
