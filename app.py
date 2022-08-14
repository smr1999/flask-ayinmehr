from flask import Flask,render_template,request

app = Flask(__name__)

auth = {"username":"ali",
        "password":"123"}


@app.route('/',methods=["GET","POST"])
def index():
    print(request.form)
    return render_template("index.html")

@app.route('/login',methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    
    if not username or not password:
        return "Error"

    if username.lower() == auth["username"] and password == auth["password"]:
        return f"Welcome user {username}"
    return "Invalid credential"