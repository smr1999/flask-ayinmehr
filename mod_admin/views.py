from flask import get_flashed_messages,render_template, request, abort, session,flash,redirect,url_for
from http import HTTPStatus
from . import admin
from .utils import admin_view
from mod_user.forms import LoginForm
from mod_user.models import User


# @admin.before_request
# def before_req():
#     print (session)
#     return ''

@admin.route('/')
@admin_view
def index():
    return 'This is admin panel'

@admin.route('/login',methods=["GET","POST"])
def login():
    login_form = LoginForm()
    if request.method.upper() == "POST":
        if not login_form.validate_on_submit():
            abort(HTTPStatus.BAD_REQUEST)
        user = User.query.filter(User.email.ilike(login_form.email.data)).first()
        if not user:
            flash("User not found !",category="danger")
            return redirect(url_for("admin.login"))
        if not user.check_password(login_form.password.data):
            flash("Invalid Password !",category="danger")
            return redirect(url_for("admin.login"))
        if not user.is_admin():
            flash("You are not admin",category="danger")
            return redirect(url_for("admin.login"))
        session["user_email"] = user.email
        session["user_id"] = user.id
        session["user_role"] = user.role
        return "Login success"
    if session.get('user_role') == 1 and session.get('user_id'):
        return "You have already logged in"
    return render_template('admin/login.html',form=login_form,title="Admin Login")