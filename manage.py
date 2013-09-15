#!/usr/bin/env python
from flask.ext.script import Manager, Server
from appname import app, db
from appname.models import *

manager = Manager(app)
manager.add_command("runserver", Server())

@manager.shell
def make_shell_context():
    return dict(app=app, user=User)

@manager.command
def createdb():
    """Creates all of the databases defined in sqlalchemy"""
    from appname.models import db
    db.create_all()

if __name__ == "__main__":
    manager.run()