from flask import render_template, request, abort, session,flash,redirect,url_for
from http import HTTPStatus
from app import db
from . import admin
from .utils import admin_view
from mod_user.forms import LoginForm,RegisterForm
from mod_user.models import User
from mod_blog.forms import CreatePostForm, ModifyCategoryForm,ModifyPostForm,CreateCategoryForm
from mod_blog.models import Category, Post

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

@admin.route('/users')
@admin_view
def list_users():
    users = User.query.order_by(User.id.desc()).all()
    return render_template('admin/list_users.html',users=users,title="List Users")

@admin.route('/users/new',methods=["GET","POST"])
@admin_view
def create_user():
    user = User()
    register_form = RegisterForm(obj=user)
    if request.method == 'POST':
        if register_form.validate_on_submit():
            register_form.populate_obj(user)
            user.set_password(register_form.password.data)
            db.session.add(user)
            db.session.commit()
            flash('Account created successfully !',category='success')
            return redirect(url_for('admin.list_users'))
        flash('Fix these bugs and then resend the form .','danger')
    return render_template('admin/create_user.html',title="Register User",form=register_form)

@admin.route('/posts')
@admin_view
def list_posts():
    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('admin/list_posts.html',posts=posts,title="List Posts")

@admin.route('/posts/new',methods=['GET','POST'])
@admin_view
def create_post():
    post = Post()
    create_post_form = CreatePostForm(obj=post)
    if request.method == 'POST':
        if create_post_form.validate_on_submit():
            create_post_form.populate_obj(post)
            db.session.add(post)
            db.session.commit()
            flash("Post created successfully","success")
            return redirect(url_for('admin.list_posts'))
        flash("Fix the errors and send form again","danger")
    return render_template('admin/create_post.html',title='Create Post',form=create_post_form)

@admin.route('/posts/delete/<int:post_id>')
@admin_view
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    flash(f'Post \"{post.title}\" deleted successfully .',category='warning')
    return redirect(url_for('admin.list_posts'))

@admin.route('/posts/modify/<int:post_id>',methods=['GET','POST'])
@admin_view
def modify_post(post_id):
    post = Post.query.get(post_id)
    modify_post_form = ModifyPostForm(obj=post)
    modify_post_form.set_post_id(post_id)
    if request.method == 'POST':
        if modify_post_form.validate_on_submit():
            modify_post_form.populate_obj(post)
            db.session.add(post)
            db.session.commit()
            flash("Post modified successfully","success")
            return redirect(url_for('admin.list_posts'))
        flash("Fix the errors and send form again","danger")
    return render_template('admin/modify_post.html',form=modify_post_form,title="Modify Post")

@admin.route('/categories')
@admin_view
def list_categories():
    categories = Category.query.order_by(Category.id.desc()).all()
    return render_template('admin/list_categories.html',categories=categories,title="List Categories")

@admin.route('/categories/new',methods=['GET','POST'])
@admin_view
def create_category():
    category = Category()
    create_category_form = CreateCategoryForm(obj=category)
    if request.method == 'POST':
        if create_category_form.validate_on_submit():
            create_category_form.populate_obj(category)
            db.session.add(category)
            db.session.commit()
            flash("Category created successfully","success")
            return redirect(url_for('admin.list_categories'))
        flash("Fix the errors and send form again","danger")
    return render_template('admin/create_category.html',title='Create Category',form=create_category_form)

@admin.route('/categories/delete/<int:category_id>')
@admin_view
def delete_category(category_id):
    category = Category.query.get_or_404(category_id)
    db.session.delete(category)
    db.session.commit()
    flash(f'Category \"{category.name}\" deleted successfully .',category='warning')
    return redirect(url_for('admin.list_categories'))

@admin.route('/categories/modify/<int:category_id>',methods=['GET','POST'])
@admin_view
def modify_category(category_id):
    category = Category.query.get(category_id)
    modify_category_form = ModifyCategoryForm(obj=category)
    modify_category_form.set_category_id(category_id)
    if request.method == 'POST':
        if modify_category_form.validate_on_submit():
            modify_category_form.populate_obj(category)
            db.session.add(category)
            db.session.commit()
            flash("Category modified successfully","success")
            return redirect(url_for('admin.list_categories'))
        flash("Fix the errors and send form again","danger")
    return render_template('admin/modify_category.html',form=modify_category_form,title="Modify Category")
