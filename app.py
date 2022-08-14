from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello world</h1>'

@app.route('/about')
def about():
    return 'this is about page'

# @app.route('/hello/<name>')
# @app.route('/hello/<string:name>')
# @app.route('/hello/<int:name>')
# @app.route('/hello/<float:name>')
# @app.route('/hello/<path:name>')
@app.route('/hello/<name>')
def hello_name(name):
    return f'Hello {name}'