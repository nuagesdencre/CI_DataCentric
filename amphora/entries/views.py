from flask import render_template, url_for, Blueprint, redirect, abort, request, flash
from flask_login import current_user, login_required

from amphora import db
from amphora.models import Story, Being
from amphora.entries.forms import EntryStory, EntryBeing

entries = Blueprint('entries', __name__)


# Create Story - Tested!
@entries.route('/new_story', methods=['GET', 'POST'])
@login_required
def create_story():
    """
    Creating a new entry of type story
    """
    form = EntryStory()

    if form.validate_on_submit():
        story = Story(title=form.title.data,
                      text=form.text.data,
                      country=form.country.data,
                      category=form.category.data,
                      source=form.source.data,
                      user_id=current_user.id)

        db.session.add(story)
        db.session.commit()
        print('Story created!')
        flash('New story created!')
        return redirect(url_for('main.repo'))
    return render_template('entries/new_story.html', form=form)


# Create Being - Tested!
@entries.route('/new_being', methods=['GET', 'POST'])
@login_required
def create_being():
    """
    Creating a new entry of type being
    """
    form = EntryBeing()

    if form.validate_on_submit():
        being = Being(name=form.name.data,
                      country=form.country.data,
                      text=form.text.data,
                      category=form.category.data,
                      source=form.source.data,
                      user_id=current_user.id)

        db.session.add(being)
        db.session.commit()
        print('New being created!')
        flash('New being created!')
        return redirect(url_for('main.repo'))
    return render_template('entries/new_being.html', form=form)


# VIEW
@entries.route('/story/<int:story_id>')
def view_story(story_id):
    """
     View a specific story entry
     """
    story = Story.query.get_or_404(story_id)
    return render_template('entries/stories.html', story=story, title=story.title,
                           text=story.text, country=story.country,
                           category=story.category, source=story.source)


@entries.route('/being/<int:being_id>')
def view_being(being_id):
    """
     View a specific being entry
     """
    being = Being.query.get_or_404(being_id)

    return render_template('entries/beings.html', being=being, name=being.name,
                           text=being.text, country=being.country,
                           category=being.category, source=being.source)


@entries.route('/story/<int:story_id>/update', methods=['GET', 'POST'])
@login_required
def update_story(story_id):
    """
     Update an existing story entry, only possible if
     user is the author of the entry
     """
    story = Story.query.get_or_404(story_id)
    if story.user != current_user:
        abort(403)

    form = EntryStory()
    if form.validate_on_submit():
        story.title = form.title.data
        story.text = form.text.data
        story.country = form.country.data
        story.source = form.source.data
        story.category = form.category.data
        db.session.commit()
        flash('Update successful!')
        print('Update successful!')
        return redirect(url_for('entries.view_story', story_id=story_id))
    form.title.data = story.title
    form.text.data = story.text
    form.country.data = story.country
    form.category.data = story.category
    form.source.data = story.source
    return render_template('entries/new_story.html', form=form)


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


# Delete Being - Tested!
@entries.route('/being/<int:being_id>/delete', methods=['GET', 'POST'])
@login_required
def delete_being(being_id):
    """
     Delete an existing being entry, only possible if
     user is the author of the entry
     """
    being = Being.query.get_or_404(being_id)
    if being.user != current_user:
        abort(403)
        flash('Permission denied')
    db.session.delete(being)
    db.session.commit()
    print('Deleted the entry.')
    return redirect(url_for('main.repo'))
