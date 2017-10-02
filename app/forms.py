from flask_wtf import Form
from wtforms import validators, StringField, PasswordField
from wtforms.widgets import TextArea
from wtforms.fields.html5 import EmailField
from wtforms.validators import ValidationError

class ContactForm(Form):
    name = StringField('Name', [validators.DataRequired()])
    email = EmailField('Email Address', [
        validators.DataRequired(), 
        validators.Email()
        ]    
    )
    message = StringField('Message',
        widget=TextArea(),
        validators=[validators.Length(max=250)]
    )