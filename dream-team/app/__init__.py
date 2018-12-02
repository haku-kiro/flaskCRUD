# Entry point for project (python level)

# Third party imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Local imports (Contains our config sections for live/dev)
from config import app_config

# db variable init
db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    # Having it so that we can set the env when creating an instance
    app.config.from_object(app_config[config_name])
    # Getting the instance config file ?
    app.config.from_pyfile('config.py')
    db.init_app(app)

    return app
