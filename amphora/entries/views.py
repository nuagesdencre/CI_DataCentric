from flask import render_template, url_for, flash, Blueprint, redirect, request
from flask_login import current_user, login_required

from amphora import db
from amphora.models import Story, Being
from amphora.entries.forms import Story, Being

entries = Blueprint('entries',__name__)

# CRUD Story, Being


@entries.route('/create_story', methods=['GET','POST'])
@login_required
def create_story():
    """
    Creating a new entry of type story
    """
    form = Story()

    if form.validate_on_submit():
        story = Story(title=form.title.data,
                      text=form.text.data,
                      user_id=current_user.id)

        db.session.add(story)
        db.session.commit()
        print('Story created!')
        return redirect(url_for('main.repo'))
    return render_template('create_story.html', form=form)