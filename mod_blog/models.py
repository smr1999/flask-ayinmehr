from app import db


class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(128), nullable=False, unique=True)
    description = db.Column(db.Text())
    slug = db.Column(db.String(64), nullable=False, unique=True)


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(128), nullable=False, unique=True)
    summary = db.Column(db.Text())
    content = db.Column(db.Text())
    slug = db.Column(db.String(64), nullable=False, unique=True)