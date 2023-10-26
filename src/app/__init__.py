from flask import Flask

from config import Config
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    from .routes.auth import auth_bp
    from .routes.users import users_bp 

    app.register_blueprint(auth_bp)
    app.register_blueprint(users_bp)


    return app