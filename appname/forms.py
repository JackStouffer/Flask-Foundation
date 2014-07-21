from flask_wtf import Form
from wtforms import TextField, PasswordField
from wtforms import validators


class LoginForm(Form):
    username = TextField(u'Username', validators=[validators.required()])
    password = PasswordField(u'Password', validators=[validators.optional()])
