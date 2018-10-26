from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


class CatForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = TextAreaField('Text', validators=[DataRequired(), Length(min=6,
                                                                    max=550, message='Minimum 6 characters')])
    picture = StringField('Picture')
    submit = SubmitField("Done!")

