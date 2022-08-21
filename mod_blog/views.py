from flask import render_template,request
from sqlalchemy import or_
from . import blog
from .models import Category, Post

@blog.route('/')
def index():
    posts = Post.query.all()
    return render_template('blog/index.html',posts=posts)

@blog.route('/<string:slug>')
def single_post(slug):
    post = Post.query.filter(Post.slug == slug).first_or_404()
    return render_template('blog/single_post.html',post=post,title=post.title)

@blog.route('/search')
def search_blog():
    search_query = request.args.get('search',default='')
    
    title_cond = Post.title.ilike(f'%{search_query}%')
    summay_cond = Post.summary.ilike(f'%{search_query}%')    
    content_cond = Post.content.ilike(f'%{search_query}%')
    found_post = Post.query.filter(or_(title_cond,summay_cond,content_cond)).all()
    
    return render_template('blog/search_post.html',posts=found_post,search=search_query,title=f'Search for \'{search_query}\'')

@blog.route('/category/<string:slug>')
def single_category(slug):
    category = Category.query.filter(Category.slug == slug).first_or_404()
    return render_template('blog/single_category.html',posts=category.posts,title=f'Category \'{category.name}',category=category)