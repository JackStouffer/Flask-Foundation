#! ../env/bin/python
# -*- coding: utf-8 -*-

import pytest

create_user = True


@pytest.mark.usefixtures("testapp")
class TestLogin:
    def test_login(self, testapp):
        """ Tests if the login form functions """

        rv = testapp.post('/login', data=dict(
            username='admin',
            password="supersafepassword"
        ), follow_redirects=True)

        assert rv.status_code == 200
        assert 'Logged in successfully.' in str(rv.data)

    def test_login_fail(self, testapp):
        """ Tests if the login form fails correctly """

        rv = testapp.post('/login', data=dict(
            username='admin',
            password=""
        ), follow_redirects=True)

        assert rv.status_code == 200
        assert 'Invalid username or password' in str(rv.data)
