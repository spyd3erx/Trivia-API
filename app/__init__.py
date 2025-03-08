from flask import Flask
from app.config import DevelopmentConfig
from app.ext import db, migrate, cors, jwt
from app.models import *

def create_app():
    """This function created a object Flask
        Retun: app: Flask
    """

    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)

    cors.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    @app.route('/')
    def index():
        return 'Hello World'

    from app.api import api_bp
    app.register_blueprint(api_bp, url_prefix='/api/v1')

    return app