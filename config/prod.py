import os

# Configurations
DEBUG = False
SECRET_KEY = "MySecretk@y"
SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
SQLALCHEMY_TRACK_MODIFICATIONS = False