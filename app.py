from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    students = ['John', 'Sara', 'Mohammad']
    numbers = list(range(1,21))
    return render_template('index.html',students=students,numbers=numbers)
