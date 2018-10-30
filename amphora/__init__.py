# vendors
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
from amphora.config import Config


app = Flask(__name__)
app.config.from_object(Config)
# flask-mail
mail = Mail(app)

# preparing user view management
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'users.login'

# Database
db = SQLAlchemy(app)
Migrate(app, db)

# amphora
from amphora.main.views import main
from amphora.users.views import users
from amphora.entries.views import entries
from amphora.categories.views import categories
from amphora.main.error.handlers import error_pages
from amphora.search.views import searchdb

# Registering blueprints
app.register_blueprint(main)
app.register_blueprint(error_pages)
app.register_blueprint(users)
app.register_blueprint(entries)
app.register_blueprint(categories)
app.register_blueprint(searchdb)


