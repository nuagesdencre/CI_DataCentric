from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, URL


class EntryStory(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(min=10,
                                                                    max=60)])
    text = TextAreaField('Text', validators=[DataRequired(), Length(min=20,
                                                                    max=950)])
    category_id = SelectField('Category', coerce=int)
    source = StringField('Reference (URL)', validators=[
        URL(require_tld=True, message=u'Invalid URL (example of a valid URL: http://www.website.com).')])
    meaning = TextAreaField('Associated Meaning and Values', validators=[DataRequired(), Length(min=20, max=250)])
    submit = SubmitField("Done!")


class EntryBeing(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=10,
                                                                  max=60)])
    text = TextAreaField('Text', validators=[DataRequired(), Length(min=20,
                                                                    max=950)])
    category_id = SelectField('Category', coerce=int)
    source = StringField('Reference (URL)', validators=[URL(require_tld=False,
                                            message=u'Invalid URL (example of a valid URL: http://www.website.com).')])
    meaning = TextAreaField('Associated Meaning and Values', validators=[DataRequired(), Length(min=20, max=250)])
    submit = SubmitField("Done!")


class CommentForm(FlaskForm):
    subject = StringField('Subject', validators=[DataRequired(), Length(min=10,
                                                                        max=60)])
    content = TextAreaField('Comment', validators=[DataRequired(), Length(min=20,
                                                                          max=950)])
    submit = SubmitField("Done!")
