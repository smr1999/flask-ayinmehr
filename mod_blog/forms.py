from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import DataRequired,ValidationError
import re
from .models import Post


class CreatePostForm(FlaskForm):
    title = StringField(label="Title",validators=[DataRequired()])
    summary = TextAreaField(label="Post summary")
    content = TextAreaField(label="Post content",validators=[DataRequired()])
    slug = StringField(label="Slug",validators=[DataRequired()])
    submit = SubmitField(label="Create Post")

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