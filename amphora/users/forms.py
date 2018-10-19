from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField
from wtforms import StringField, PasswordField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo,Length
from flask_login import current_user
from amphora.models import User


class Login(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log in!')


class Register(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6,
                                                                            max=30, message='Minimum 6 characters'),
                                                     EqualTo('psw_again')])
    psw_again = PasswordField('Confirm Password', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Register now!')

    # check if methods can be inherited or something similar to avoid repetition
    def unique_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email has already been registered!')

    def unique_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username has already been registered!')


class Update(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    profile_pic = FileField('Picture!', validators=[FileAllowed(['png','jpg'])])
    submit = SubmitField('Update your info!')

    # check if methods can be inherited or something similar to avoid repetition
    def unique_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email has already been registered!')

    def unique_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username has already been registered!')