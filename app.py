from flask import Flask,render_template

# app = Flask(__name__)
app = Flask(__name__,template_folder="templates")

# @app.route('/')
# def index():
#     return """
#     <!Doctype html>
#     <html>
#         <head>
#             <title>
#             My Flask App 
#             </title>
#         </head>
#         <body>
#             <h1>Hello World!</h1>
#         </body>
#     </html>
#     """

@app.route('/')
def index():
    return render_template('index.html')