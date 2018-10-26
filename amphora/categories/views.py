from flask import render_template, url_for, Blueprint, redirect, abort, request, flash
from amphora import db
from amphora.models import Category, Story, Being
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
        return redirect(url_for('categories.all_categories'))
    return render_template('categories/new_category.html', form=form)


@categories.route('/category/<int:category_id>')
def view_category(category_id):
    """
     View a specific category details
     """
    category = Category.query.get_or_404(category_id)
    stories = Story.query.filter_by(category=category)
    beings = Being.query.filter_by(category=category)
    return render_template('categories/view_category.html', stories=stories, beings=beings,
                           category=category, name=category.name,
                           picture=category.picture, description=category.description
                           )


@categories.route('/category/<int:category_id>/update', methods=['GET', 'POST'])
def update_category(category_id):
    """
     Update an existing category
     """
    category = Category.query.get_or_404(category_id)
    form = CatForm()
    if form.validate_on_submit():
        category.name = form.name.data
        category.description = form.description.data
        category.picture = form.picture.data
        db.session.commit()
        flash('Update successful!')
        print('Update successful!')
        return redirect(url_for('categories.view_category', category_id=category_id))
    form.name.data = category.name
    form.description.data = category.description
    form.picture.data = category.picture
    return render_template('categories/new_category.html', form=form)


@categories.route('/all_categories')
def all_categories():
    """
    View all categories
    """
    categories = Category.query.order_by(Category.name)
    return render_template('categories/all_categories.html', categories=categories)
