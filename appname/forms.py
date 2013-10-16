from flask_wtf import Form
from wtforms import TextField, TextAreaField
from wtforms import validators


class MyForm(Form):
    user_name = TextField(u'First Name', validators=[validators.required()])
    message = TextAreaField(u'message', validators=[validators.optional()])
