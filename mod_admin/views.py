from flask import get_flashed_messages,render_template, request, abort, session,flash,redirect,url_for
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
            flash("User not found !",category="danger")
            return redirect(url_for("admin.login"))
        if not user.check_password(login_form.password.data):
            flash("Invalid Password !",category="danger")
            return redirect(url_for("admin.login"))
        session["email"] = user.email
        session["id"] = user.id
        return "Login success"
    if session.get("email") is not None:
        return "You have already logged in"    
    return render_template('admin/login.html',form=login_form,title="Admin Login")