from flask import request,render_template,flash,redirect,url_for
from app import db
from . import user
from .models import User
from .forms import RegisterForm
from .utils import delete_redis, generate_token,send_register_email,decode_token,find_redis


@user.route('/register',methods=['GET','POST'])
def register():
    register_form = RegisterForm()
    if request.method == 'POST':
        if register_form.validate_on_submit():
            user = User(fullname=register_form.fullname.data,email=register_form.email.data)
            user.set_password(register_form.password.data)
            db.session.add(user)
            db.session.commit()
            token = generate_token(user,mode='register')
            if send_register_email(user,token):
                flash('You have create your account successfully ! check your email to confirm your email .',category='success')
            else :
                flash('Somthing wrong to send email .',category='danger')
                # todo : remove from redis
                db.session.remove(user)
                db.session.commit()
            return redirect(url_for('user.register'))
        flash('Fix these bugs and then resend the form .','danger')
    return render_template('user/register.html',title="Register User",form=register_form)

@user.route('/confirm/<token>')
def confirm_register(token):
    decoded_token = decode_token(token)
    if decoded_token:
        user_id = decoded_token.get('user_id')
        mode = decoded_token.get('mode')
        key = decoded_token.get('key')
        name = f'{user_id}_{mode}'
        user = User.query.get(int(user_id))
        if user and not user.active:
            true_key = find_redis(name)
            if true_key and true_key.decode('utf-8') == key:
                delete_redis(name=name)
                user.active = True
                db.session.add(user)
                db.session.commit()
                flash('User activated success fully',category='success')
                return redirect(url_for('home'))
    flash('Invalid token or user activated .',category='danger')
    return redirect(url_for('user.register'))