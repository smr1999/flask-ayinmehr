from flask import Flask

app = Flask(__name__)

@app.route('/index')
@app.route('/hello-world')
def hello_world():
    name = 'Mammad'
    return f'Hello {name}'


@app.route('/index2')
def hello_world2():
    return 'Hello world from /index2'