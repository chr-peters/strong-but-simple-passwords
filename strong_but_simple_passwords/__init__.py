from flask import Flask
from whitenoise import WhiteNoise
from pathlib import Path
from .config import get_config_from_env_vars
from . import views


def create_app(config=None):
    # don't use a static_folder since we will use whitenoise to serve the static files
    app = Flask(__name__, static_folder=None)

    if config is None:
        config = get_config_from_env_vars()

    app.config.from_object(config)

    app.add_url_rule("/", "index", view_func=views.index, methods=("GET", "POST"))

    # use whitenoise to serve static files
    static_root = Path(__file__).parent / "static/"
    app.wsgi_app = WhiteNoise(app.wsgi_app, root=static_root, prefix="static/")

    return app
