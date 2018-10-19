from flask import render_template, request, Blueprint, abort


main = Blueprint('main', __name__)


@main.route('/')
def index():
    """
    Landing page
    """
    return render_template('index.html')


@main.route('/repo')
def repo():
    """
    Accessing the repository
    """
    return render_template('repo.html')


@main.route('/about')
def about():
    """
    Information about Amphora and the project
    """
    return render_template('about.html')


@main.route('/contact')
def contact():
    """
    Contact information
    """
    return render_template('contact.html')