from flask import Flask, g,request
import sqlite3

app = Flask(__name__)


def create_db():
    return sqlite3.connect('./db.sqlite3')


@app.before_request
def before_request():
    g.db = create_db()
    g.cur = g.db.cursor()
    print("before")


@app.after_request
def after_request(response):
    g.db.close()
    print("after")
    return response


@app.route('/')
def index():
    action = request.args.get('action')
    username = request.args.get('username')
    password = request.args.get('password')
    if action and username and password :
        if action.lower() == 'register':
            try:
                g.cur.execute('INSERT INTO users(username,password) values (?,?)',(
                username,password
            )) # Do not use fstring because for example fstring can not convert None(python) to null(SQL)
                g.db.commit()
                return 'User added'
            except sqlite3.IntegrityError:
                g.db.rollback()
                return 'username dupplicated'
        elif action.lower() == 'login':
            g.cur.execute('SELECT * FROM users WHERE username = ? AND password = ?',(username,password))
            user = g.cur.fetchone()
            if user:
                return f'Welcome User {user[1]}'
            else:
                return 'User not found'      
    print("index view")
    return 'Hello world'
