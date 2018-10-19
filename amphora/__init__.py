# vendors
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# amphora
from amphora.main.views import main
from amphora.error.handlers import error_pages

app = Flask(__name__)

# preparing user view management
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'users.login'

# Database
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Migrate(app, db)


# Registering blueprints
app.register_blueprint(main)
app.register_blueprint(error_pages)