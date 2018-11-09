from flask import render_template, Blueprint, redirect, url_for
from sqlalchemy import or_
from amphora.models import User, Category, Story, Being, Comment
from amphora.search.forms import SearchForm

searchdb = Blueprint('searchdb', __name__)


@searchdb.route('/search', methods=['GET', 'POST'])
def search():
    form = SearchForm()
    if form.validate_on_submit():
        query = str(form.query.data).lower()
        return redirect(url_for('searchdb.search_req', query=query))
    return render_template('search/search.html', form=form)


@searchdb.route('/search/<query>')
def search_req(query):
    """
     Query database
     """
    categories = Category.query.filter(or_(Category.name.ilike("%{}%".format(query)), Category.description.ilike("%{}%".format(query))))
    stories = Story.query.filter(or_(Story.title.ilike("%{}%".format(query)), Story.meaning.ilike("%{}%".format(query)),
                                     Story.text.ilike("%{}%".format(query))))
    beings = Being.query.filter(or_(Being.name.ilike("%{}%".format(query)), Being.meaning.ilike("%{}%".format(query)),
                                    Being.text.ilike("%{}%".format(query))))
    users = User.query.filter(or_(User.username.ilike("%{}%".format(query)), User.email.ilike("%{}%".format(query))))
    comments = Comment.query.filter(or_(Comment.subject.ilike("%{}%".format(query)), Comment.content.ilike("%{}%".format(query))))
    return render_template('search/results.html', stories=stories, beings=beings,
                           categories=categories, users=users, comments=comments)
