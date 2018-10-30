from flask import render_template, Blueprint,request,redirect, url_for
from amphora import db
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
    categories = Category.query.filter(or_(Category.name.contains(query), Category.description.contains(query)))
    stories = Story.query.filter(or_(Story.title.contains(query), Story.meaning.contains(query),
                                     Story.text.contains(query)))
    beings = Being.query.filter(or_(Being.name.contains(query), Being.meaning.contains(query),
                                    Being.text.contains(query)))
    users = User.query.filter(or_(User.username.contains(query), User.email.contains(query)))
    comments = Comment.query.filter(or_(Comment.subject.contains(query), Comment.content.contains(query)))
    return render_template('search/results.html', stories=stories, beings=beings,
                           categories=categories, users=users, comments=comments)