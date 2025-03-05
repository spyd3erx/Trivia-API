from dotenv import load_dotenv
import os

load_dotenv()

class Config():
    SECRET_KEY = os.getenv("SECRET_KEY")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = f"sqlite:///db.sqlite3"
    DEBUG=True