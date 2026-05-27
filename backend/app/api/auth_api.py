from flask import Blueprint, request, jsonify, session

from app.config.db import db

from app.models.user_model import User


auth_bp = Blueprint("auth", __name__)


# HOME API
@auth_bp.route("/")
def home():

    return {
        "message": "FleetFlow Backend Running"
    }


# REGISTER API
@auth_bp.route("/api/auth/register", methods=["POST"])
def register():

    data = request.json

    existing_user = User.query.filter_by(
        email=data["email"]
    ).first()

    if existing_user:

        return jsonify({

            "success": False,

            "message": "Email already exists"

        }), 400

    new_user = User(

        name=data["name"],

        email=data["email"],

        password=data["password"],

        role=data.get("role", "manager")

    )

    db.session.add(new_user)

    db.session.commit()

    return jsonify({

        "success": True,

        "message": "User registered successfully"

    })


# LOGIN API
@auth_bp.route("/api/auth/login", methods=["POST"])
def login():

    data = request.json

    user = User.query.filter_by(
        email=data["email"]
    ).first()

    if not user:

        return jsonify({

            "success": False,

            "message": "Invalid email"

        }), 401

    if user.password != data["password"]:

        return jsonify({

            "success": False,

            "message": "Invalid password"

        }), 401

    # CREATE SESSION
    session["user_id"] = user.id
    print(session)

    session["role"] = user.role

    return jsonify({

        "success": True,

        "message": "Login successful",

        "user": {

            "id": user.id,

            "name": user.name,

            "email": user.email,

            "role": user.role

        }

    })


# GET AUTHENTICATED USER API
@auth_bp.route(
    "/api/auth/get-authenticated-user",
    methods=["GET"]
)
def get_authenticated_user():

    user_id = session.get("user_id")

    if not user_id:

        return jsonify({

            "success": False,

            "message": "User not authenticated"

        }), 401

    user = User.query.get(user_id)

    if not user:

        return jsonify({

            "success": False,

            "message": "User not found"

        }), 404

    return jsonify({

        "success": True,

        "user": {

            "id": user.id,

            "name": user.name,

            "email": user.email,

            "role": user.role

        }

    })