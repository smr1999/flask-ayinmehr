from flask import Blueprint

blog = Blueprint('blog',__name__,url_prefix="/blog",template_folder='templates')

from . import models,views