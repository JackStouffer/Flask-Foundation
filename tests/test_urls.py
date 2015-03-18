#! ../env/bin/python
# -*- coding: utf-8 -*-

import pytest

create_user = True


@pytest.mark.usefixtures("testapp")
class TestURLs:
    def test_home(self, testapp):
        """ Tests if the home page loads """

        rv = testapp.get('/')
        assert rv.status_code == 200

    def test_login(self, testapp):
        """ Tests if the login page loads """

        rv = testapp.get('/login')
        assert rv.status_code == 200

    def test_logout(self, testapp):
        """ Tests if the logout page loads """

        rv = testapp.get('/logout')
        assert rv.status_code == 302

    def test_restricted_logged_out(self, testapp):
        """ Tests if the restricted page returns a 302
            if the user is logged out
        """

        rv = testapp.get('/restricted')
        assert rv.status_code == 302

    def test_restricted_logged_in(self, testapp):
        """ Tests if the restricted page returns a 200
            if the user is logged in
        """

        testapp.post('/login', data=dict(
            username='admin',
            password="supersafepassword"
        ), follow_redirects=True)

        rv = testapp.get('/restricted')
        assert rv.status_code == 200
