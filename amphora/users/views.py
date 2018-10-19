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
