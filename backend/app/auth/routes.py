from flask import Blueprint

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/")

def home():

    return {
        "message": "Backend Running Successfully"
    }