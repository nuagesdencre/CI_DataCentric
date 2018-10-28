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
    name = StringField('Name', validators=[DataRequired(), Length(min=6,
                                                                    max=60)])
    description = TextAreaField('Description', validators=[DataRequired(), Length(min=6,
                                                                    max=550)])
    submit = SubmitField("Done!")

