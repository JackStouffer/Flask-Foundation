#!/usr/bin/env python

import os

from flask_script import Manager, Server
from flask_script.commands import ShowUrls, Clean
from appname import create_app
from appname.models import db, User

# default to dev config because no one should use this in
# production anyway
env = os.environ.get('APPNAME_ENV', 'dev')
app = create_app('appname.settings.%sConfig' % env.capitalize())

manager = Manager(app)
manager.add_command("server", Server())
manager.add_command("show-urls", ShowUrls())
manager.add_command("clean", Clean())


@manager.shell
def make_shell_context():
    """ Creates a python REPL with several default imports
        in the context of the app
    """

    return dict(app=app, db=db, User=User)


@manager.command
def createdb():
    """ Creates a database with all of the tables defined in
        your SQLAlchemy models
    """

    db.create_all()


@manager.command
def add_user():
    """ Creates a new user """
    username = raw_input("Username: ")
    password = getpass()

    if User.query.filter_by(username=username).count():
        sys.exit("User by that name already exists")

    db.session.add(User(username, password))
    db.session.commit()


if __name__ == "__main__":
    manager.run()
