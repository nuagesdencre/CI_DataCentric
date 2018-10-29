from flask import render_template, url_for, Blueprint, redirect, abort, request, flash
from flask_login import current_user, login_required

from amphora import db
from amphora.models import Story, Being, Category, Comment
from amphora.entries.forms import EntryStory, EntryBeing, CommentForm

entries = Blueprint('entries', __name__)


@entries.route('/new_story', methods=['GET', 'POST'])
@login_required
def create_story():
    """
    Creating a new entry of type story
    """
    form = EntryStory()
    form.category_id.choices = [(i.id, i.name) for i in Category.query.all()]
    if form.validate_on_submit():
        story = Story(title=form.title.data,
                      text=form.text.data,
                      meaning=form.meaning.data,
                      category_id=form.category_id.data,
                      source=form.source.data,
                      user_id=current_user.id)

        db.session.add(story)
        db.session.commit()
        print('Story created!')
        flash('New story created!')
        return redirect(url_for('main.repo'))
    return render_template('entries/new_story.html', form=form)


@entries.route('/new_being', methods=['GET', 'POST'])
@login_required
def create_being():
    """
    Creating a new entry of type being
    """
    form = EntryBeing()
    form.category_id.choices = [(i.id, i.name) for i in Category.query.all()]
    if form.validate_on_submit():
        being = Being(name=form.name.data,
                      meaning=form.meaning.data,
                      text=form.text.data,
                      category_id=form.category_id.data,
                      source=form.source.data,
                      user_id=current_user.id)

        db.session.add(being)
        db.session.commit()
        print('New being created!')
        flash('New being created!')
        return redirect(url_for('main.repo'))
    return render_template('entries/new_being.html', form=form)


# VIEW
@entries.route('/story/<int:story_id>', methods=['GET', 'POST'])
def view_story(story_id):
    """
     View a specific story entry
     """
    story = Story.query.get_or_404(story_id)
    comments = Comment.query.filter_by(story_id=story_id)
    form = CommentForm()
    if form.validate_on_submit():
        comments = Comment(subject=form.subject.data,
                           content=form.content.data,
                           story_id=story.id,
                           being_id=None,
                           user_id=current_user.id)
        db.session.add(comments)
        db.session.commit()
        print('Comment created!')
        return redirect(url_for('entries.view_story', story_id=story_id))
    return render_template('entries/stories.html', story=story, title=story.title,
                           text=story.text, meaning=story.meaning, source=story.source, comments=comments,
                           form=form)

# Todo: fix anonymoususermixin id or request login for post action

@entries.route('/being/<int:being_id>', methods=['GET', 'POST'])
def view_being(being_id):
    """
     View a specific being entry
     """
    being = Being.query.get_or_404(being_id)
    comments = Comment.query.filter_by(being_id=being_id)
    form = CommentForm()

    if form.validate_on_submit():
        comments = Comment(subject=form.subject.data,
                           content=form.content.data,
                           being_id=being.id,
                           story_id=None,
                           user_id=current_user.id)
        db.session.add(comments)
        db.session.commit()
        print('Comment created!')
        return redirect(url_for('entries.view_being', being_id=being_id))
    return render_template('entries/beings.html', being=being, name=being.name,
                           text=being.text, meaning=being.meaning,
                           source=being.source, comments=comments, form=form)


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
    form.category_id.choices = [(i.id, i.name) for i in Category.query.all()]
    if form.validate_on_submit():
        story.title = form.title.data
        story.text = form.text.data
        story.meaning = form.meaning.data
        story.source = form.source.data
        story.category_id = form.category_id.data
        db.session.commit()
        flash('Update successful!')
        print('Update successful!')
        return redirect(url_for('entries.view_story', story_id=story_id))
    form.title.data = story.title
    form.text.data = story.text
    form.meaning.data = story.meaning
    form.category_id.data = story.category_id
    form.source.data = story.source
    title = form.title.data
    return render_template('entries/new_story.html', form=form, title=title)


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
    form.category_id.choices = [(i.id, i.name) for i in Category.query.all()]
    if form.validate_on_submit():
        being.name = form.name.data
        being.text = form.text.data
        being.meaning = form.meaning.data
        being.category_id = form.category_id.data
        being.source = form.source.data
        db.session.commit()
        flash('Update successful!')
        print('Update successful!')
        return redirect(url_for('entries.view_being', being_id=being_id))
    form.name.data = being.name
    form.text.data = being.text
    form.meaning.data = being.meaning
    form.category_id.data = being.category_id
    form.source.data = being.source
    title = form.name.data
    return render_template('entries/new_being.html', form=form, title=title)


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


