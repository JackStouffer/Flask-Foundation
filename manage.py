#!/usr/bin/env python
from flask.ext.script import Manager, Server
from appname import app

manager = Manager(app)
manager.add_command("runserver", Server())

@manager.shell
def make_shell_context():
    return dict(app=app)

@manager.command
def createdb():
    """Creates all of the databases defined in sqlalchemy"""
    from appname.models import db
    db.create_all()

if __name__ == "__main__":
    manager.run()