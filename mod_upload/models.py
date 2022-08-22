from datetime import datetime
from app import db
from sqlalchemy import DateTime,String

class File(db.Model):
    __tablename__ = 'files'
    id = db.Column(db.Integer(),primary_key=True)
    filename = db.Column(db.String(256),nullable=False,unique=True)
    upload_date = db.Column(db.DateTime,default=datetime.utcnow,nullable=False)