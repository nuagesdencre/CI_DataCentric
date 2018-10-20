from flask import render_template, url_for, flash, Blueprint, redirect, request
from flask_login import current_user, login_user, logout_user, login_required

from amphora import db
from amphora.models import User, Story, Being
from amphora.users.forms import Login, Register, Update

# login, logout, account, user entries

users = Blueprint('users', __name__)


@users.route('/register', methods=['GET', 'POST'])
def register():
    """
    Where users provide their information in order to register.
    """
    form = Register()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('users.login'))
    return render_template('users/register.html', form=form)


@users.route('/login', methods=['GET', 'POST'])
def login():
    """
    Where users, who are already registered, can log in. The form checks for matching passwords (hashed).
    """
    form = Login()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user.psw_check(form.password.data) and user is not None:
            login_user(user)
            flash('You are now logged in!')
    return render_template('users/login.html', form=form)


@users.route('/logout')
def logout():
    """
    Where users can log out.
    """
    logout_user()
    return redirect(url_for('main.index'))


@users.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    """
    Where users can view their details and update them, once logged in
    """
    form = Update()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit
        return redirect(url_for('users.account'))
    form.username.data = current_user.username
    form.email.data = current_user.email
    profile_pic = url_for('static', filename='img/'+current_user.profile_pic)
    return render_template('users/account.html', profile_pic=profile_pic, form=form)


@users.route('/<username>')
def user_entries(username):
    """
     Where we can see entries authored by a specific user
    """
    user = User.query.filter_by(username=username).first()
    stories = Story.query.filter_by(user)
    beings = Being.query.filter_by(user)
    return render_template('users/entries.html', user=user, stories=stories, beings=beings)