from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Development

app = Flask(__name__)
app.config.from_object(Development)
app.jinja_options
# initilize dependencies
db = SQLAlchemy(app)
migrate = Migrate(app,db)

# Register Blueprints
from mod_admin import admin
app.register_blueprint(admin)

from mod_user import user
app.register_blueprint(user)

from mod_blog import blog
app.register_blueprint(blog)

# Main app
import views