#! ../env/bin/python
# -*- coding: utf-8 -*-
from appname import create_app
from appname.models import db, User


class TestForm:
    def setup(self):
        app = create_app('appname.settings.DevConfig', env='dev')
        self.app = app.test_client()
        db.app = app
        db.create_all()
        admin = User('admin', 'supersafepassword')
        db.session.add(admin)
        db.session.commit()

    def teardown(self):
        db.session.remove()
        db.drop_all()

    def test_user_login(self):
        rv = self.app.post('/login', data=dict(
            username='admin',
            password="supersafepassword"
        ), follow_redirects=True)

        assert rv.status_code == 200
        assert 'Logged in successfully.' in rv.data
