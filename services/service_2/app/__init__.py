from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

def create_app(configName='config'):
    app = Flask(__name__)
    app.config.from_object(configName)
    db = SQLAlchemy(app)
    Migrate(app, db, render_as_batch=True)
    return app, db

app, db = create_app()

from app import views

db.create_all()