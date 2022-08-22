from flask import Blueprint

upload = Blueprint('upload',__name__,template_folder='templates')

from . import models