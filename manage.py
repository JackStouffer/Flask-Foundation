#!/usr/bin/env python

import os
import urllib

import click
from flask import current_app, url_for
from flask.cli import FlaskGroup

from appname import create_app
from appname.models import db


def create_app_with_config(*args):
    # default to dev config because no one should use this in
    # production anyway
    env = os.environ.get('APPNAME_ENV', 'dev')
    return create_app('appname.settings.%sConfig' % env.capitalize())


@click.group(cls=FlaskGroup, create_app=create_app_with_config)
def cli():
    pass


@cli.command()
def create_all():
    """ Creates a database with all of the tables defined in
        your SQLAlchemy models
    """

    db.create_all()


@cli.command()
def show_urls():
    """ List all of the endpoints on the app and the supportted methods
    """
    output = []
    for rule in current_app.url_map.iter_rules():
        options = {}
        for arg in rule.arguments:
            options[arg] = "<{0}>".format(arg)

        methods = ','.join(rule.methods)
        url = url_for(rule.endpoint, **options)
        line = urllib.parse.unquote("{:45s} {:30s} {}".format(rule.endpoint, methods, url))
        output.append(line)

    for line in sorted(output):
        print(line)


if __name__ == "__main__":
    cli()
