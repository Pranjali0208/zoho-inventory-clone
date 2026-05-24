from flask import Flask
from flask_cors import CORS
from app.config.db import db
from app.auth.routes import auth_bp
import os

def create_app():

    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")

    CORS(app, supports_credentials=True)

    db.init_app(app)

    app.register_blueprint(auth_bp)

    return app