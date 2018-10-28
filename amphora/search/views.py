from flask import render_template, Blueprint,request,redirect, url_for
from amphora import db

from amphora.models import User, Category, Story, Being
from amphora.search.forms import SearchForm

searchdb = Blueprint('searchdb', __name__)


@searchdb.route('/search', methods=['GET', 'POST'])
def search():
    form = SearchForm()
    if form.validate_on_submit():
        query = str(form.query.data).lower()
        print(query)
        return redirect(url_for('searchdb.search_req', query=query))
    return render_template('search/search.html', form=form)


@searchdb.route('/search/<query>')
def search_req(query):
    """
     Query database
     """
    categories = Category.query.filter_by(query=query)
    stories = Story.query.filter_by(query=query)
    beings = Being.query.filter_by(query=query)
    users = User.query.filter_by(query=query)
    return render_template('search/results.html', stories=stories, beings=beings,
                           categories=categories, users=users)