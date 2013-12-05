#! ../env/bin/python
# -*- coding: utf-8 -*-
from appname import create_app
from appname.models import db


class TestForm:
    def setup(self):
        app = create_app('appname.settings.DevConfig', env='dev')
        self.app = app.test_client()
        db.app = app
        db.create_all()

    def teardown(self):
        db.session.remove()
        db.drop_all()

    def test_user_form_empty(self):
        rv = self.app.post('/wtform', data=dict(
            user_name="",
            message=""
        ), follow_redirects=True)

        assert rv.status_code == 200
        assert 'There was a problem submitting the form!' in rv.data

    def test_user_form_message(self):
        rv = self.app.post('/wtform', data=dict(
            user_name="",
            message="test message"
        ), follow_redirects=True)

        assert rv.status_code == 200
        assert 'There was a problem submitting the form!' in rv.data

    def test_user_form_name(self):
        rv = self.app.post('/wtform', data=dict(
            user_name="admin",
            message=""
        ), follow_redirects=True)

        assert rv.status_code == 200
        assert 'The form was successfully submitted' in rv.data

    def test_user_form_both(self):
        rv = self.app.post('/wtform', data=dict(
            user_name="admin",
            message="test message"
        ), follow_redirects=True)

        assert rv.status_code == 200
        assert 'The form was successfully submitted' in rv.data
