from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Length, Email, EqualTo, DataRequired, ValidationError

class AddMessageForm(FlaskForm):

    fullname = StringField(validators=[DataRequired()])
    email = StringField(validators=[Email(), DataRequired()])
    countries = StringField(validators=[DataRequired()])
    submit = SubmitField()
