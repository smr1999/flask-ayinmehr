from flask import request,render_template,flash,redirect,url_for
from app import db
from . import user
from .models import User
from .forms import RegisterForm


@user.route('/register',methods=['GET','POST'])
def register():
    register_form = RegisterForm()
    if request.method == 'POST':
        if register_form.validate_on_submit():
            user = User(fullname=register_form.fullname.data,email=register_form.email.data)
            user.set_password(register_form.password.data)
            db.session.add(user)
            db.session.commit()
            flash('You have create your account successfully !')
            return redirect(url_for('user.register'))
        flash('Fix these bugs and then resend the form .')
    return render_template('user/register.html',title="Register User",form=register_form)