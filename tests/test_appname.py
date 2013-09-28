#! ../env/bin/python
# -*- coding: utf-8 -*-
from appname import create_app
from appname.models import db, User


class TestConfig:
    def test_dev_config(self):
        app = create_app('appname.settings.DevConfig', env='dev')

        assert app.config['DEBUG'] is True
        assert app.config['SQLALCHEMY_DATABASE_URI'] == 'sqlite:///../database.db'
        assert app.config['SQLALCHEMY_ECHO'] is True
        assert app.config['CACHE_TYPE'] == 'null'

    def test_prod_config(self):
        app = create_app('appname.settings.ProdConfig', env='prod')

        assert app.config['SQLALCHEMY_DATABASE_URI'] == 'sqlite:///../database.db'
        assert app.config['CACHE_TYPE'] == 'simple'


class TestModels:
    def setup(self):
        app = create_app('appname.settings.DevConfig', env='dev')
        self.app = app.test_client()
        db.app = app
        db.create_all()

    def teardown(self):
        db.session.remove()
        db.drop_all()

    def test_user(self):
        admin = User('admin', 'supersafepassword')

        assert admin.username == 'admin'
        assert admin.password == 'supersafepassword'

        db.session.add(admin)
        db.session.commit()


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
