from flask import (
    Blueprint,
    request,
    jsonify
)

from app.config.db import db
from app.models.supplier_model import Supplier

supplier_bp = Blueprint(
    "supplier",
    __name__
)
@supplier_bp.route(
    "/api/suppliers",
    methods=["POST"]
)
def create_supplier():

    data = request.json

    existing_supplier = Supplier.query.filter_by(
        email=data["email"]
    ).first()

    if existing_supplier:

        return jsonify({

            "success": False,

            "message": "Supplier already exists"

        }), 400

    supplier = Supplier(

        name=data["name"],

        email=data["email"],

        phone=data.get("phone"),

        country=data.get(
            "country",
            "Oman"
        )

    )

    db.session.add(supplier)

    db.session.commit()

    return jsonify({

        "success": True,

        "message": "Supplier created successfully"

    })
@supplier_bp.route(
    "/api/suppliers",
    methods=["GET"]
)
def get_suppliers():

    suppliers = Supplier.query.all()

    data = []

    for supplier in suppliers:

        data.append({

            "id": supplier.id,

            "name": supplier.name,

            "email": supplier.email,

            "phone": supplier.phone,

            "country": supplier.country

        })

    return jsonify({

        "success": True,

        "count": len(data),

        "data": data

    })
@supplier_bp.route(
    "/api/suppliers/<int:supplier_id>",
    methods=["GET"]
)
def get_supplier(supplier_id):

    supplier = Supplier.query.get(
        supplier_id
    )

    if not supplier:

        return jsonify({

            "success": False,

            "message": "Supplier not found"

        }), 404

    return jsonify({

        "success": True,

        "data": {

            "id": supplier.id,

            "name": supplier.name,

            "email": supplier.email,

            "phone": supplier.phone,

            "country": supplier.country

        }

    })
@supplier_bp.route(
    "/api/suppliers/<int:supplier_id>",
    methods=["PUT"]
)
def update_supplier(supplier_id):

    supplier = Supplier.query.get(
        supplier_id
    )

    if not supplier:

        return jsonify({

            "success": False,

            "message": "Supplier not found"

        }), 404

    data = request.json

    supplier.name = data.get(
        "name",
        supplier.name
    )

    supplier.email = data.get(
        "email",
        supplier.email
    )

    supplier.phone = data.get(
        "phone",
        supplier.phone
    )

    supplier.country = data.get(
        "country",
        supplier.country
    )

    db.session.commit()

    return jsonify({

        "success": True,

        "message": "Supplier updated successfully"

    })
@supplier_bp.route(
    "/api/suppliers/<int:supplier_id>",
    methods=["DELETE"]
)
def delete_supplier(supplier_id):

    supplier = Supplier.query.get(
        supplier_id
    )

    if not supplier:

        return jsonify({

            "success": False,

            "message": "Supplier not found"

        }), 404

    db.session.delete(supplier)

    db.session.commit()

    return jsonify({

        "success": True,

        "message": "Supplier deleted successfully"

    })