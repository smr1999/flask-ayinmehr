from flask_wtf import FlaskForm
from sqlalchemy import and_
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import DataRequired,ValidationError
import re
from .models import Post,Category
from .utils.form import MultipleCheckBoxField

class CreatePostForm(FlaskForm):
    title = StringField(label="Post title",validators=[DataRequired()])
    summary = TextAreaField(label="Post summary")
    content = TextAreaField(label="Post content",validators=[DataRequired()])
    slug = StringField(label="Post slug",validators=[DataRequired()])
    categories_ = MultipleCheckBoxField(label="Categories",choices=[],coerce=int)
    submit = SubmitField(label="Create post")

    def validate_title(self,title):
        post = Post.query.filter(Post.title == self.title.data).first()
        if post : 
            raise ValidationError("Title dupplicated . Try another title .")

    def validate_slug(self,slug):
        post = Post.query.filter(Post.slug == self.slug.data).first()
        if post : 
            raise ValidationError("Slug dupplicated . Try another slug .")
        if not re.search("^[a-z0-9]+(?:-[a-z0-9]+)*$", str(self.slug.data)):
            raise ValidationError("Invalid slug pattern")

class ModifyPostForm(FlaskForm):
    title = StringField(label="Post title",validators=[DataRequired()])
    summary = TextAreaField(label="Post summary")
    content = TextAreaField(label="Post content",validators=[DataRequired()])
    slug = StringField(label="Post slug",validators=[DataRequired()])
    categories_ = MultipleCheckBoxField(label="Categories",choices=[],coerce=int)
    submit = SubmitField(label="Modify post")

    def set_post_id(self,post_id):
        self.post_id = post_id
    
    def validate_title(self,title):
        post = Post.query.filter(and_(Post.title == self.title.data, Post.id != self.post_id)).first()
        if post : 
            raise ValidationError("Title dupplicated . Try another title .")

    def validate_slug(self,slug):
        post = Post.query.filter(and_(Post.slug == self.slug.data, Post.id != self.post_id)).first()
        if post : 
            raise ValidationError("Slug dupplicated . Try another slug .")
        if not re.search("^[a-z0-9]+(?:-[a-z0-9]+)*$", str(self.slug.data)):
            raise ValidationError("Invalid slug pattern")

class CreateCategoryForm(FlaskForm):
    name = StringField(label="Category name",validators=[DataRequired()])
    description = TextAreaField(label="Category description")
    slug = StringField(label="Category slug",validators=[DataRequired()])
    submit = SubmitField(label="Create category")

    def validate_name(self,name):
        category = Category.query.filter(Category.name == self.name.data).first()
        if category :
            raise ValidationError("Category name dupplicated . Try another name .")

    def validate_slug(self,slug):
        category = Category.query.filter(Category.slug == self.slug.data).first()
        if category:
            raise ValidationError("Slug dupplicated . Try another slug .")
        if not re.search("^[a-z0-9]+(?:-[a-z0-9]+)*$", str(self.slug.data)):
            raise ValidationError("Invalid slug pattern")

class ModifyCategoryForm(FlaskForm):
    name = StringField(label="Category name",validators=[DataRequired()])
    description = TextAreaField(label="Category description")
    slug = StringField(label="Category slug",validators=[DataRequired()])
    submit = SubmitField(label="Modify category")

    def set_category_id(self,category_id):
        self.category_id = category_id

    def validate_name(self,name):
        category = Category.query.filter(and_(Category.name == self.name.data, Category.id != self.category_id)).first()
        if category :
            raise ValidationError("Category name dupplicated . Try another name .")

    def validate_slug(self,slug):
        category = Category.query.filter(and_(Category.slug == self.slug.data, Category.id != self.category_id)).first()
        if category:
            raise ValidationError("Slug dupplicated . Try another slug .")
        if not re.search("^[a-z0-9]+(?:-[a-z0-9]+)*$", str(self.slug.data)):
            raise ValidationError("Invalid slug pattern")

class SearchForm(FlaskForm):
    search = StringField(label='Serach',validators=[DataRequired()])
    submit = SubmitField(label="Search")