from flask import Flask
from indiewar.settings import config


def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'development')

    app = Flask('indiewar')
    app.config.from_object(config[config_name])
