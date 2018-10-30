from flask import render_template, url_for, flash, Blueprint, redirect, request
from flask_login import current_user, login_user, logout_user, login_required

from amphora import db
from amphora.models import User, Story, Being, Comment
from amphora.users.forms import Login, Register, Update, ResetPsw, ResetPswReq
from amphora.users.email import send_password_reset_email

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
                    psw=form.password.data)
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
    error_message=''
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user.psw_check(form.password.data) and user is not None:
            login_user(user)
            return redirect(url_for('users.account'))
        else:
            error_message = 'The login details provided are incorrect.'
    return render_template('users/login.html', form=form, error_message=error_message)


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
        current_user.email = form.email.data
        db.session.commit()
        return redirect(url_for('users.account'))
    form.email.data = current_user.email
    username = current_user.username
    email = current_user.email
    return render_template('users/account.html', username=username, email=email, form=form)


@users.route('/<username>')
def user_entries(username):
    """
     Where we can see entries authored by a specific user
    """
    user = User.query.filter_by(username=username).first_or_404()
    stories = Story.query.filter_by(user=user)
    beings = Being.query.filter_by(user=user)
    comments = Comment.query.filter_by(user=user)
    return render_template('users/entries.html', user=user, beings=beings, stories=stories, comments=comments)


@users.route('/reset_password_request', methods=['GET', 'POST'])
def reset_psw_req():
    if current_user.is_authenticated:
        return redirect(url_for('users.account'))
    form = ResetPswReq()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            send_password_reset_email(user)
        flash('Your password reset has been requested.')
        return redirect(url_for('users.login'))
    return render_template('users/reset_psw_req.html',
                           title='Reset Password', form=form)


@users.route('/reset_psw/<token>', methods=['GET', 'POST'])
def reset_psw(token):
    if current_user.is_authenticated:
        return redirect(url_for('users.account'))
    user = User.verify_reset_password_token(token)
    if not user:
        return redirect(url_for('main.index'))
    form = ResetPsw()
    if form.validate_on_submit():
        user.set_password(form.password.data)
        db.session.commit()
        flash('Your password has been reset.')
        return redirect(url_for('users.login'))
    return render_template('users/psw_reset.html', form=form)