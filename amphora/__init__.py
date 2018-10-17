from flask import Flask
from amphora.main.views import main


app = Flask(__name__)

app.register_blueprint(main)