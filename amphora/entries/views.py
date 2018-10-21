from flask import render_template, url_for, Blueprint, redirect, abort
from flask_login import current_user, login_required

from amphora import db
from amphora.models import Story, Being
from amphora.entries.forms import Story, Being

entries = Blueprint('entries', __name__)


# CRUD Story, Being
# NEW


@entries.route('/new_story', methods=['GET', 'POST'])
@login_required
def new_story():
    """
    Creating a new entry of type story
    """
    form = Story()

    if form.validate_on_submit():
        story = Story(title=form.title.data,
                      text=form.text.data,
                      country=form.country.data,
                      category=form.category.data,
                      user_id=current_user.id)

        db.session.add(story)
        db.session.commit()
        print('Story created!')
        return redirect(url_for('main.repo'))
    return render_template('entries/new_story.html', form=form)


@entries.route('/new_being', methods=['GET', 'POST'])
@login_required
def new_being():
    """
    Creating a new entry of type being
    """
    form = Being()

    if form.validate_on_submit():
        being = Being(name=form.name.data,
                      text=form.text.data,
                      country=form.country.data,
                      category=form.category.data,
                      user_id=current_user.id)

        db.session.add(being)
        db.session.commit()
        print('New being created!')
        return redirect(url_for('main.repo'))
    return render_template('entries/new_being.html', form=form)


# VIEW
@entries.route('/<int:story_id>')
def story(story_id):
    """
     View a specific story
     """
    story = Story.query.get_or_404(story_id)
    return render_template('stories.html', title=story.title,
                           text=story.text, country=story.country,
                           category=story.category)


@entries.route('/<int:being_id>')
def being(being_id):
    """
     View a specific being
     """
    being = Being.query.get_or_404(being_id)
    return render_template('beings.html', title=being.title,
                           text=being.text, country=being.country,
                           category=being.category)


@entries.route('/<int:story_id/update>', methods=['GET', 'POST'])
@login_required
def update_story(story_id):
    """
     Update an existing story entry, only possible if
     user is the author of the entry
     """
    story = Story.query.get_or_404(story_id)
    if story.user != current_user:
        abort(403)
        # forbidden action
        # possibly allow for certain fields to be updated by other people?
    form = Story()
    if form.validate_on_submit():
        story.name = form.name.data,
        story.text = form.text.data,
        story.country = form.country.data,
        story.category = form.category.data
        db.session.add(story)
        db.session.commit()
        print('Update successful!')
        return redirect(url_for('story.story', story_id=story_id))


@entries.route('/<int:being_id/update>', methods=['GET', 'POST'])
@login_required
def update_being(being_id):
    """
     Update an existing being entry, only possible if
     user is the author of the entry
     """
    being = Being.query.get_or_404(being_id)
    if being.user != current_user:
        abort(403)
        # forbidden action
        # possibly allow for certain fields to be updated by other people?
    form = Being()
    if form.validate_on_submit():
        being.name = form.name.data,
        being.text = form.text.data,
        being.country = form.country.data,
        being.category = form.category.data
        db.session.add(being)
        db.session.commit()
        print('Update successful!')
        return redirect(url_for('being.being', being_id=being_id))
