import os
FLASK_APP='index.py'
FLASK_ENV='development'
SECRET_KEY='you-will-never-guess'
MONGODB_HOST='mongodb'
MONGODB_DB='app'

FLASK_APP = os.environ["FLASK_APP"]
FLASK_ENV = os.environ["FLASK_ENV"]
SECRET_KEY = os.environ["SECRET_KEY"]
MONGODB_HOST = os.environ["MONGODB_HOST"]
MONGODB_DB = os.environ["MONGODB_DB"]

