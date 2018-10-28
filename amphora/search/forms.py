from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length
from wtforms import ValidationError


class SearchForm(FlaskForm):
    query = StringField('What are you looking for?', validators=[DataRequired()])
    submit = SubmitField("Search")