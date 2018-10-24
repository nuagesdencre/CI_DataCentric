from flask import render_template, request, Blueprint, abort
from amphora.models import Story, Being


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
    page = request.args.get('page', 1, type=int)
    stories = Story.query.order_by(Story.id.desc()).paginate(page,3,False)
    beings = Being.query.order_by(Being.id.desc()).paginate(page, 3,False)
    return render_template('repo.html', stories=stories,page=page, beings=beings)


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