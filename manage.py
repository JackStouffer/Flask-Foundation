#!/usr/bin/env python
import os

from flask.ext.script import Manager, Server
from appname import create_app
from appname.models import db, User

env = os.environ.get('APPNAME_ENV', 'prod')
app = create_app('appname.settings.%sConfig' % env.capitalize(), env=env)

manager = Manager(app)
manager.add_command("server", Server())


@manager.shell
def make_shell_context():
    """ Creates a python REPL with several default imports
        in the context of the app
    """

    return dict(app=app, User=User)


@manager.command
def createdb():
    """ Creates a database with all of the tables defined in
        your Alchemy models
    """

    db.create_all()

if __name__ == "__main__":
    manager.run()
