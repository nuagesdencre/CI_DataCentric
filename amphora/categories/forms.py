from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length
from wtforms import ValidationError
from amphora.models import Category


class ValidationMixin:
    def validate_name(self, field):
        name = Category.query.filter_by(name=field.data).first()
        if name is not None:
            raise ValidationError('This category has already been created.')


class CatForm(FlaskForm, ValidationMixin):
    name = StringField('Name', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired(), Length(min=6,
                                                                    max=550,
                                                    message='Minimum 6 characters, maximum 550 characters.')])
    picture = StringField('Picture')
    submit = SubmitField("Done!")

