#! ../env/bin/python
import os

from flask import Flask, render_template
from flask_assets import Environment
from webassets.loaders import PythonLoader as PythonAssetsLoader

# from models import *
import assets

app = Flask(__name__)

# Import the config for the proper environment 
env = os.environ.get('EXAMPLE_ENV', 'dev')
app.config.from_object('appname.settings.%sConfig' % env.capitalize())
app.config['ENV'] = env

# Import and register the different asset bundles
assets_env = Environment(app)
assets_loader = PythonAssetsLoader(assets)
for name, bundle in assets_loader.load_bundles().iteritems():
    assets_env.register(name, bundle)

@app.route('/')
def hello_world():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
