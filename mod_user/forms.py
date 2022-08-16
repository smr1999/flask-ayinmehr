from flask_wtf import FlaskForm
from wtforms import EmailField,PasswordField,SubmitField,StringField
from wtforms.validators import DataRequired,EqualTo,Email,ValidationError
from .models import User

class LoginForm(FlaskForm):
    email = EmailField(label="Email",validators=[DataRequired()])
    password = PasswordField(label="Password",validators=[DataRequired()])
    submit = SubmitField(label="Login")

class RegisterForm(FlaskForm):
    fullname = StringField(label='Full Name')
    email = EmailField(label='Email',validators=[DataRequired(),Email()])
    password = PasswordField(label='Password',validators=[DataRequired()])
    password_confirm = PasswordField(label='Password Confirm',validators=[EqualTo('password')])
    submit = SubmitField(label='Register')

    def validate_email(self,email):
        user = User.query.filter(User.email.ilike(self.email.data)).first()
        if user:
            raise ValidationError("Email dupplicated, Enter another email.")