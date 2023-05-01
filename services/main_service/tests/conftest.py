import pytest

@pytest.fixture()
def app():
    from app import app

    # other setup can go here

    yield app

    # clean up / reset resources here

@pytest.fixture()
def client(app):
    return app.test_client()