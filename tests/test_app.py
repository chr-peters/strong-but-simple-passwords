from strong_but_simple_passwords import create_app
import os


def test_custom_config():
    class Config:
        SECRET_KEY = "custom-secret-key"
        TESTING = True

    app = create_app(Config)

    assert app.config["SECRET_KEY"] == "custom-secret-key"
    assert app.testing


def test_config_from_env_vars():
    os.environ["SECRET_KEY"] = "secret-key-from-env-var"

    app = create_app()

    assert app.config["SECRET_KEY"] == "secret-key-from-env-var"
    assert not app.testing
