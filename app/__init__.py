from flask import Flask
from flask_pymongo import PyMongo
from dotenv import load_dotenv
import os

mongo = PyMongo()

def create_app():
    load_dotenv()
    app = Flask(__name__)
    app.config["MONGO_URI"] = os.getenv("MONGO_URI")

    mongo.init_app(app)

    from .routes import healthme
    app.register_blueprint(healthme)

    return app

