from werkzeug.security import generate_password_hash,check_password_hash
from app import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer(),primary_key=True)
    email = db.Column(db.String(128),unique=True,nullable=False)
    password = db.Column(db.String(128),nullable=False)
    role = db.Column(db.Integer(),default=0)
    fullname = db.Column(db.String(64),nullable=True,unique=False)

    def set_password(self,password):
        self.password = generate_password_hash(password)
    
    def check_password(self,password):
        return check_password_hash(self.password,password)

    def is_admin(self):
        return self.role == 1