from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .utils import constants

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = constants.BASE_URI_DB
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from .posts import posts_bp
    from .weather import weather_bp

    db.create_all(app=app)

    app.register_blueprint(posts_bp, url_prefix='/api')
    app.register_blueprint(weather_bp, url_prefix='/api')

    return app
