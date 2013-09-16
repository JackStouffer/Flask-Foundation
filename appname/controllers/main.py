from flask import Blueprint, render_template, flash, request
from flask_wtf import Form
from wtforms import TextField, TextAreaField
from wtforms import validators

from appname import cache
from appname.models import *

main = Blueprint('main', __name__)


class MyForm(Form):
    user_name = TextField(u'First Name', validators=[validators.required()])
    message = TextAreaField(u'message', validators=[validators.optional()])


@main.route('/')
@cache.cached(timeout=1000)
def home():
    return render_template('index.html')


@main.route('/wtform', methods=['GET', 'POST'])
@cache.cached(timeout=1000)
def wtform():
    form = MyForm()
    
    if request.method == 'GET':
        return render_template('wtform_example.html', form=form)
    elif request.method == 'POST':
        if form.validate_on_submit():
            flash("The form was successfully submitted", 'success')
        else:
            flash("There was a problem submitting the form!", 'danger')
        return render_template('wtform_example.html', form=form)

