import os

# set testing to false
TESTING = True
# database in memory
SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
# set sql settings
SQLALCHEMY_TRACK_MODIFICATIONS = False
# set wtf settings
WTF_CSRF_ENABLED = True
# set secret key
SECRET_KEY = 'a-very-secret-secret'