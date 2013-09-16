#! ../env/bin/python
import os

from flask import Flask
from flask_assets import Environment
from webassets.loaders import PythonLoader as PythonAssetsLoader
from flask_sqlalchemy import SQLAlchemy
from flask.ext.cache import Cache
from flask_debugtoolbar import DebugToolbarExtension

import assets

app = Flask(__name__)

# Import the config for the proper environment using the shell var APPNAME_ENV
env = os.environ.get('APPNAME_ENV', 'prod')
app.config.from_object('appname.settings.%sConfig' % env.capitalize())
app.config['ENV'] = env

# Setup and import SQLAlchemy and the created models
db = SQLAlchemy(app)

# Setup flask cache
cache = Cache(app)
from controllers.main import main

# Import and register the different asset bundles
assets_env = Environment(app)
assets_loader = PythonAssetsLoader(assets)
for name, bundle in assets_loader.load_bundles().iteritems():
    assets_env.register(name, bundle)

# Setup flask debug-toolbar
toolbar = DebugToolbarExtension(app)

app.register_blueprint(main)

if __name__ == '__main__':
    app.run()
