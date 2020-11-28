from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField, IntegerField, StringField
from wtforms.validators import DataRequired


class ContactForm(FlaskForm):
    answers = TextAreaField("Example: 1) Answer for number 1", validators=[DataRequired()])
    assignment_id = IntegerField()
    activity = StringField()
    day = StringField()
    subject = StringField()
    week = StringField()
    submit = SubmitField("Submit Assignment")

