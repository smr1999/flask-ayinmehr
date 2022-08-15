from flask import Flask,render_template,request
from forms import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

@app.route('/')
def index():
    login_form = LoginForm()
    return render_template('index.html',form=login_form)


@app.route('/login',methods=['POST'])
def login():
    login_form = LoginForm(request.form)
    if not login_form.validate_on_submit():
        print(login_form.errors)
        return "Error"
    return "OK"