from flask import Flask,request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://flask:password@localhost:3306/flask_tut'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer(),primary_key=True)
    username = db.Column(db.String(length=32),nullable=False,unique=True) # String can translate to char or varchar
    password = db.Column(db.String(128),nullable=False)



@app.route('/')
def index():
    action = request.args.get('action')
    username = request.args.get('username')
    password = request.args.get('password')

    if action and username and password:
        if action.lower() == 'login':
            user = User.query.filter(username==username and password==password).first()
            if not user:
                return 'User not found'
            return f'Welcome user {user.username}'
        elif action.lower() == 'register':
            try :
                user = User(username=username,password=password)
                db.session.add(user)
                db.session.commit()
                return 'User created successfully'
            except IntegrityError:
                db.session.rollback()
                return 'User duplicated'
            
    return 'Hello world'
