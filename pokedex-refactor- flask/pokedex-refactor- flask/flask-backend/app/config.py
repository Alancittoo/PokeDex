import os

class Configuration(object):
    SECRET_KEY = os.environ.get("SECRET_KEY")
    FLASK_RUN_PORT = os.environ.get("FLASK_RUN_PORT")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False