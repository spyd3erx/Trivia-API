from flask import Flask
from app.config import DevelopmentConfig
from app.ext import db, migrate, cors, jwt, limiter
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
    limiter.init_app(app)

    #configurar rutas y swagger
    from app.api import create_api
    create_api(app)


    return app