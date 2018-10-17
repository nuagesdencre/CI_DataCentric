from flask import Flask
from amphora.main.views import main
from amphora.error.handlers import error_pages

app = Flask(__name__)

# registering blueprints
app.register_blueprint(main)
app.register_blueprint(error_pages)