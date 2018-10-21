from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


class Story(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    text = TextAreaField('Text', validators=[DataRequired()])
    category = StringField('Text')
    country = StringField('Associated Country', validators=[DataRequired()])
    submit = SubmitField("Done!")


class Being(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    text = TextAreaField('Text', validators=[DataRequired()])
    category = StringField('Text')
    country = StringField('Associated Country', validators=[DataRequired()])
    submit = SubmitField("Done!")