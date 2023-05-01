import pytest
from app import db

@pytest.fixture()
def app():
    from app import app
    
    # switch to test config
    app.config.from_object("config_test")
    
    with app.app_context():
       db.create_all()

    # other setup can go here

    yield app

    # clean up / reset resources here
    
    with app.app_context():
        db.drop_all()

@pytest.fixture()
def client(app):
    return app.test_client()