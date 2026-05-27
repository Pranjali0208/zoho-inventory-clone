from flask import Flask

from flask_cors import CORS

from flask_session import Session

from dotenv import load_dotenv

import os

from app.config.db import db

from app.api.auth_api import auth_bp


load_dotenv()


def create_app():

    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")


    # SESSION CONFIG
    app.config["SESSION_TYPE"] = "filesystem"

    app.config["SESSION_PERMANENT"] = False

    app.config["SESSION_USE_SIGNER"] = True

    app.config["SESSION_COOKIE_HTTPONLY"] = True

    app.config["SESSION_COOKIE_SAMESITE"] = "Lax"

    app.config["SESSION_COOKIE_SECURE"] = False


    Session(app)


    db.init_app(app)


    CORS(

        app,

        supports_credentials=True,

        origins=["http://localhost:9000"]

    )


    app.register_blueprint(auth_bp)

    return app