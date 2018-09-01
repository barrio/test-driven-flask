from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension

from config import config


# Create plugins
toolbar = DebugToolbarExtension()


def create_app(config_name):
    app = Flask(__name__)

    # Read config from config.py depending on FLASK_CONFIG
    app.config.from_object(config[config_name])

    # Init plugins
    toolbar.init_app(app)

    # Register blueprints
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
