from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


class EntryStory(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    text = TextAreaField('Text', validators=[DataRequired()])
    category = StringField('Category')
    country = StringField('Associated Country', validators=[DataRequired()])
    submit = SubmitField("Done!")


class EntryBeing(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    text = TextAreaField('Text', validators=[DataRequired()])
    category = StringField('Category')
    country = StringField('Associated Country', validators=[DataRequired()])
    submit = SubmitField("Done!")