from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField
from wtforms import StringField, PasswordField, SubmitField
from wtforms import ValidationError
from wtforms.validators import DataRequired, Email, EqualTo,Length
from flask_login import current_user
from amphora.models import User


class ValidationMixin:

    # making sure the username and email address are not already in the user table

    def validate_email(self, field):
        user = User.query.filter_by(email=field.data).first()
        if user is not None:
            raise ValidationError('This email address has already been registered.')

    def validate_username(self, field):
        user = User.query.filter_by(username=field.data).first()
        if user is not None:
            raise ValidationError('This username is already taken.')


class Login(FlaskForm):
    """
    Login Form
    """
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(message='Password is incorrect.')])
    submit = SubmitField('Log in!')


class Register(FlaskForm, ValidationMixin):
    """
    Registration Form
    """
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6,
                                                                            max=30, message='Minimum 6 characters'),
                                                     EqualTo('psw_again', message='The passwords do not match.')])
    psw_again = PasswordField('Confirm Password', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Register now!')


class Update(FlaskForm, ValidationMixin):
    """
    Update Information on Account Form
    """
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Update Email')


class ResetPswReq(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')


class ResetPsw(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    psw_again = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')