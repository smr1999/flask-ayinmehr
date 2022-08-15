from flask import Blueprint

admin = Blueprint("admin",__name__,url_prefix="/admin")

@admin.route('/index')
def index():
    return 'admin index'