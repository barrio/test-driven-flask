from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy

from config import config


# Create plugins
db = SQLAlchemy()
toolbar = DebugToolbarExtension()


def create_app(config_name):
    app = Flask(__name__)

    # Read config from config.py depending on FLASK_CONFIG
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # Init plugins
    db.init_app(app)
    toolbar.init_app(app)

    # Register blueprints
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
