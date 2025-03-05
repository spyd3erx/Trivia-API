from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restx import Api
from flask_cors import CORS


db = SQLAlchemy() #DB instance
migrate = Migrate() #system of migrations
cors = CORS() #Cors
api = Api()
