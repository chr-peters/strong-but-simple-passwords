import pytest
from strong_but_simple_passwords import create_app


class TestConfig:
    SECRET_KEY = "something-secret"
    TESTING = True


@pytest.fixture
def app():
    return create_app(TestConfig)


@pytest.fixture
def client(app):
    return app.test_client()
