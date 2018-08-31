from flask import Flask

from config import config


# Create plugin objects here


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    print(f"DEBUG: {app.config['DEBUG']}")

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
