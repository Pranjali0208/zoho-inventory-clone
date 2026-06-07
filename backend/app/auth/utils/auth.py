from functools import wraps
from flask import session, jsonify
from app.models.user_model import User


def requires_auth(f):

    @wraps(f)
    def decorated(*args, **kwargs):

        user_id = session.get("user_id")

        if not user_id:

            return jsonify({

                "success": False,

                "message": "User not authenticated"

            }), 401

        return f(*args, **kwargs)

    return decorated

from functools import wraps
from flask import session, jsonify


def requires_auth(f):

    @wraps(f)

    def decorated(*args, **kwargs):

        user_id = session.get("user_id")

        if not user_id:

            return jsonify({

                "success": False,

                "message": "User not authenticated"

            }), 401

        return f(*args, **kwargs)

    return decorated


def get_current_user():

    user_id = session.get("user_id")

    if not user_id:
        return None

    return User.query.get(user_id)