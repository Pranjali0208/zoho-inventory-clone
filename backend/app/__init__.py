from flask import Flask

from flask_cors import CORS

from flask_session import Session

from dotenv import load_dotenv
from flask_migrate import Migrate
import os
from app.api.product_api import product_bp
from app.api.supplier_api import supplier_bp
from app.config.db import db
from app.api.analytics_api import analytics_bp
from app.api.auth_api import auth_bp
from app.api.invoice_api import invoice_bp
from app.api.dashboard_api import dashboard_bp
from app.api.inventory_transaction_api import (inventory_transaction_bp)
migrate = Migrate()

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
    migrate.init_app(app, db)


    CORS(

        app,

        supports_credentials=True,

        origins=["http://localhost:9000"]

    )


    app.register_blueprint(auth_bp)
    app.register_blueprint(invoice_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(analytics_bp)
    app.register_blueprint(supplier_bp)
    app.register_blueprint(inventory_transaction_bp)
    app.register_blueprint(product_bp)

    return app