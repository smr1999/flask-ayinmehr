from multiprocessing import context
from flask import render_template, request, abort, session,flash,redirect,url_for
from http import HTTPStatus
from app import db
from . import admin
from .utils import admin_view
from mod_user.forms import LoginForm
from mod_user.models import User
from mod_blog.forms import CreatePostForm
from mod_blog.models import Post

# @admin.before_request
# def before_req():
#     print (session)
#     return ''

@admin.route('/')
@admin_view
def index():
    return render_template('admin/index.html',title="Admin dashboard")

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
        return redirect(url_for('admin.index'))
    if session.get('user_role') == 1 and session.get('user_id'):
        return redirect(url_for('admin.index'))
    return render_template('admin/login.html',form=login_form,title="Admin Login")

@admin.route('/logout',methods=['GET'])
@admin_view
def logout():
    session.clear()
    flash('You logged out successfully .',category='warning')
    return redirect(url_for('admin.login'))

@admin.route('/posts/new',methods=['GET','POST'])
@admin_view
def create_post():
    create_post_form = CreatePostForm()
    if request.method == 'POST':
        if create_post_form.validate_on_submit():
            post = Post(title=create_post_form.title.data,summary=create_post_form.summary.data,content=create_post_form.content.data,slug=create_post_form.slug.data)
            db.session.add(post)
            db.session.commit()
            flash("Post created successfully","success")
            return redirect(url_for('admin.index'))
        flash("Fix the errors and send form again","danger")
    return render_template('admin/create_post.html',title='Create Post',form=create_post_form)