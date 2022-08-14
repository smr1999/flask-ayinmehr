from flask import Flask,request

app = Flask(__name__)


# @app.route('/',methods=["GET","POST"])
# def index():
#     result = f"Request Method : {request.method} \
#     <br> Request Args : {request.args} \
#     <br> Request Form : {request.form}"
#     return result

@app.route('/',methods=["GET","POST"])
def index():
    name = request.args.get('name') or request.form.get('name')
    return f"Hello {name}"
