from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


class CatForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=6,
                                                                    max=60)])
    description = TextAreaField('Description', validators=[DataRequired(), Length(min=6,
                                                                    max=550)])
    submit = SubmitField("Done!")

