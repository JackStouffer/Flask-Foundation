#! ../env/bin/python
# -*- coding: utf-8 -*-
from appname import create_app
from appname.models import db, User


class TestModels:
    def setup(self):
        app = create_app('appname.settings.DevConfig', env='dev')
        self.app = app.test_client()
        db.app = app
        db.create_all()

    def teardown(self):
        db.session.remove()
        db.drop_all()

    def test_user_save(self):
        """ Test Saving the user model """
        admin = User('admin', 'supersafepassword')
        db.session.add(admin)
        db.session.commit()
        
        user = User.query.filter_by(username="admin").first()
        assert user is not None
        
    def test_user_password(self):
        """ Test password hashing and checking """
        admin = User('admin', 'supersafepassword')

        assert admin.username == 'admin'
        assert admin.check_password('supersafepassword')
