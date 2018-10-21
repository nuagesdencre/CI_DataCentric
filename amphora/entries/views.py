from flask import render_template, url_for, flash, Blueprint, redirect, request
from flask_login import current_user, login_required

from amphora import db
from amphora.models import Story, Being
from amphora.entries.forms import Story, Being

entries = Blueprint('entries',__name__)

# CRUD Story, Being
#NEW

@entries.route('/new_story', methods=['GET','POST'])
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


@entries.route('/new_being', methods=['GET','POST'])
@login_required
def new_being():
    """
    Creating a new entry of type being
    """
    form = Being()

    if form.validate_on_submit():
        being = Being(Name=form.title.data,
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
    story = Story.query.get_or_404(story_id)
    return render_template('stories.html', title=story.title,
                           text=story.text, country=story.country,
                           category=story.category)