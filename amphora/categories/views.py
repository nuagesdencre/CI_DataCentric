from flask import render_template, url_for, Blueprint, redirect, abort, request, flash
from flask_login import current_user, login_required

from amphora import db
from amphora.models import Category
from amphora.categories.forms import CatForm

categories = Blueprint('categories', __name__)


@categories.route('/new_category', methods=['GET', 'POST'])
def create_category():
    """
    Creating a new category
    """
    form = CatForm()

    if form.validate_on_submit():
        category = Category(name=form.name.data, picture=form.picture.data,
                            description=form.description.data)

        db.session.add(category)
        db.session.commit()
        print('Category created!')
        return redirect(url_for('main.repo'))
    return render_template('categories/new_cat.html', form=form)


# VIEW
@categories.route('/category/<int:category_id>')
def view_category(category_id):
    """
     View a specific category details
     """
    story = Story.query.get_or_404(story_id)
    return render_template('entries/stories.html', story=story, title=story.title,
                           text=story.text, country=story.country,
                           category=story.category, source=story.source)


@entries.route('/being/<int:being_id>/update', methods=['GET', 'POST'])
@login_required
def update_being(being_id):
    """
     Update an existing being entry, only possible if
     user is the author of the entry
     """
    being = Being.query.get_or_404(being_id)
    if being.user != current_user:
        abort(403)

    form = EntryBeing()
    if form.validate_on_submit():
        being.name = form.name.data
        being.text = form.text.data
        being.country = form.country.data
        being.category = form.category.data
        being.source = form.source.data
        db.session.commit()
        flash('Update successful!')
        print('Update successful!')
        return redirect(url_for('entries.view_being', being_id=being_id))
    form.name.data = being.name
    form.text.data = being.text
    form.country.data = being.country
    form.category.data = being.category
    form.source.data = being.source
    return render_template('entries/new_being.html', form=form)


# Delete Story - Tested!
@entries.route('/story/<int:story_id>/delete', methods=['GET', 'POST'])
@login_required
def delete_story(story_id):
    """
     Delete an existing story entry, only possible if
     user is the author of the entry
     """
    story = Story.query.get_or_404(story_id)
    if story.user != current_user:
        abort(403)
        flash('Permission denied')
    db.session.delete(story)
    db.session.commit()
    print('Deleted the entry.')
    return redirect(url_for('main.repo'))

