from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField
from wtforms import StringField, PasswordField, SubmitField
from wtforms import ValidationError
from wtforms.validators import DataRequired, Email, EqualTo,Length
from flask_login import current_user
from amphora.models import User


class ValidationMixin:
 # fix validation and error messages

    def unique_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email has already been registered!')

    def unique_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username has already been registered!')


class Login(FlaskForm):
    """
    Login Form
    """
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log in!')


class Register(FlaskForm, ValidationMixin):
    """
    Registration Form
    """
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6,
                                                                            max=30, message='Minimum 6 characters'),
                                                     EqualTo('psw_again', message='Password does not match.')])
    psw_again = PasswordField('Confirm Password', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Register now!')


class Update(FlaskForm, ValidationMixin):
    """
    Update Information on Account Form
    """
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    profile_pic = FileField('Picture!', validators=[FileAllowed(['png','jpg'])])
    submit = SubmitField('Update your info!')

