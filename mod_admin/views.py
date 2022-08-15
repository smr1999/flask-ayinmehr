from flask import session
from . import admin


@admin.route('/index')
def index():
    return 'admin index'

@admin.route('/login')
def login():
    session.clear()
    print(session)
    return "1"