from flask import render_template, request, abort, session
from . import admin
from mod_user.forms import LoginForm
from mod_user.models import User


@admin.route('/index')
def index():
    return 'admin index'

@admin.route('/login',methods=["GET","POST"])
def login():
    login_form = LoginForm()
    if request.method.upper() == "POST":
        if not login_form.validate_on_submit():
            abort(400)
        user = User.query.filter(User.email.ilike(login_form.email.data)).first()
        if not user:
            # abort(400)
            return "Invalid credentials" , 400
        if not user.check_password(login_form.password.data):
            return "Invalid credentials" , 400
        session["email"] = user.email
        session["id"] = user.id
        return "Login success"
    if session.get("email") is not None:
        return "You have already logged in"    
    return render_template('login.html',form=login_form)