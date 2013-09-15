#! ../env/bin/python
import os

from flask import Flask, render_template
from flask_assets import Environment
from webassets.loaders import PythonLoader as PythonAssetsLoader
from flask_sqlalchemy import SQLAlchemy

import assets
from controllers.main import main

app = Flask(__name__)

# Import the config for the proper environment 
env = os.environ.get('EXAMPLE_ENV', 'prod')
app.config.from_object('appname.settings.%sConfig' % env.capitalize())
app.config['ENV'] = env

db = SQLAlchemy(app)
from models import *

# Import and register the different asset bundles
assets_env = Environment(app)
assets_loader = PythonAssetsLoader(assets)
for name, bundle in assets_loader.load_bundles().iteritems():
    assets_env.register(name, bundle)

app.register_blueprint(main)

if __name__ == '__main__':
    app.run()
