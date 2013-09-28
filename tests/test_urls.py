#! ../env/bin/python
# -*- coding: utf-8 -*-
from appname import create_app
from appname.models import db


class TestURLs:
    def setup(self):
        app = create_app('appname.settings.DevConfig', env='dev')
        self.app = app.test_client()
        db.app = app
        db.create_all()

    def teardown(self):
        db.session.remove()
        db.drop_all()

    def test_home(self):
        rv = self.app.get('/')
        assert rv.status_code == 200

    def test_form(self):
        rv = self.app.get('/wtform')
        assert rv.status_code == 200
