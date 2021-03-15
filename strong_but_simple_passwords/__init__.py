from flask import Flask
from .config import get_config_from_env_vars
from . import views


def create_app(config=None):
    app = Flask(__name__)

    if config is None:
        config = get_config_from_env_vars()

    app.config.from_object(config)

    app.add_url_rule("/", "index", view_func=views.index, methods=("GET", "POST"))

    return app
