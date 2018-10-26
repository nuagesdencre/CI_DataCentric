from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length


class EntryStory(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    text = TextAreaField('Text', validators=[DataRequired(), Length(min=6,
                                                                    max=950, message='Minimum 6 characters')])
    category_id = SelectField('Category', coerce=int)
    source = StringField('Reference (URL)')
    country = StringField('Associated Country', validators=[DataRequired()])
    submit = SubmitField("Done!")


class EntryBeing(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=6,
                                                                  max=60, message='Minimum 6 characters')])
    text = TextAreaField('Text', validators=[DataRequired(), Length(min=6,
                                                                    max=950, message='Minimum 6 characters')])
    category_id = SelectField('Category', coerce=int)
    source = StringField('Reference (URL)')
    country = StringField('Associated Country', validators=[DataRequired(), Length(min=6,
                                                                                   max=60,
                                                                                   message='Minimum 6 characters')])
    submit = SubmitField("Done!")

