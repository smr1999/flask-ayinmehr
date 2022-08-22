from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail
from redis import Redis
from config import Development

app = Flask(__name__)
app.config.from_object(Development)

# initilize dependencies
db = SQLAlchemy(app)
migrate = Migrate(app,db)
mail = Mail(app)
redis = Redis.from_url(app.config.get('REDIS_SERVER_URL'))

# Register Blueprints
from mod_admin import admin
app.register_blueprint(admin)

from mod_user import user
app.register_blueprint(user)

from mod_blog import blog
app.register_blueprint(blog)

from mod_upload import upload
app.register_blueprint(upload)

# Main app
import views,context_proccesor