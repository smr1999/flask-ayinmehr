from flask import render_template
from flask_mail import Message
from random import randint
import jwt
from threading import Thread
from app import app,redis,mail

def generate_token(user,mode):
    key = randint(1000,9999)
    token = jwt.encode({'user_id':user.id,'mode':mode,'key':str(key)},key=app.config.get('SECRET_KEY'),algorithm='HS256')
    name = f'{user.id}_{mode}'
    redis.set(name=name,value=key,ex=4*60*60) # 4 hours for expire
    return token

def async_mail(app,msg):
    with app.app_context():
        mail.send(msg)

def send_register_email(user,token):
    try:
        sender = app.config.get('MAIL_USERNAME')
        recipients = [user.email]
        subject = 'Register User - Confirm'
        html = render_template('user/email/confirm_email.html',token=token)
        msg = Message(sender=sender,recipients=recipients,subject=subject,html=html)
        Thread(target=async_mail,args=(app,msg)).start()
        return True
    except Exception as e:
        return False

def decode_token(token):
    try : 
        decoded_token = jwt.decode(token,key=app.config.get('SECRET_KEY'),algorithms=['HS256'])
        return decoded_token
    except Exception as e:
        return None

def find_redis(name):
    return redis.get(name=name)

def delete_redis(name):
    return redis.delete(name)