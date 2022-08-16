from app import db

post_category = db.Table('posts_categories', db.metadata,
                         db.Column('category_id', db.Integer(), db.ForeignKey(
                             'categories.id', ondelete='CASCADE')),
                         db.Column('post_id', db.Integer(), db.ForeignKey(
                             'posts.id', ondelete='CASCADE'))
                         )


class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(128), nullable=False, unique=True)
    description = db.Column(db.Text())
    slug = db.Column(db.String(64), nullable=False, unique=True)
    posts = db.relationship(
        "Post", secondary=post_category, backref=db.backref("categories", lazy="dynamic"), lazy="dynamic"
    )


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(128), nullable=False, unique=True)
    summary = db.Column(db.Text())
    content = db.Column(db.Text())
    slug = db.Column(db.String(64), nullable=False, unique=True)
