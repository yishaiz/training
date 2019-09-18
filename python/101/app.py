from flask import Flask
from flask import request


app = Flask('hello-world')


@app.route('/')
def hello():
    return ("Hello World - python flask")


@app.route('/other')
def other():
    return ("other route")

if __name__ == '__main__':
    app.run()


