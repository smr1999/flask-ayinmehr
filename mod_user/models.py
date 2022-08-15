from app import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer(),primary_key=True)
    email = db.Column(db.String(128),unique=True,nullable=False)
    password = db.Column(db.String(128),nullable=False)
    role = db.Column(db.Integer(),default=0)
    fullname = db.Column(db.String(64),nullable=True,unique=False)