import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager   #user login and sessions
from flask_bcrypt import Bcrypt

# Instances
db = SQLAlchemy()
bootstrap = Bootstrap()
login_manger = LoginManager()
login_manger.login_view = 'authentication.login'
login_manger.session_protection = 'strong'
bcrypt = Bcrypt()


def create_app(config_type):  # dev,prod,test
    app = Flask(__name__)

    configuration = os.path.join(os.getcwd(), 'config', config_type+'.py')

    app.config.from_pyfile(configuration)
    db.init_app(app)
    bootstrap.init_app(app)
    login_manger.init_app(app)
    bcrypt.init_app(app)

    from app.catalog import main
    app.register_blueprint(main)

    from app.auth import authentication
    app.register_blueprint(authentication)
    return app