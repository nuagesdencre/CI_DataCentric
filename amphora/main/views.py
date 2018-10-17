from flask import render_template, request, Blueprint, abort


main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/contact')
def contact():
    return render_template('contact.html')