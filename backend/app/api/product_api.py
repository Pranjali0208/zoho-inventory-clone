from flask import (
    Blueprint,
    request,
    jsonify
)

from app.config.db import db
from app.models.product_model import Product

product_bp = Blueprint(
    "product",
    __name__
)
@product_bp.route(
    "/api/products",
    methods=["POST"]
)
def create_product():

    data = request.json

    product = Product(

        name=data["name"],

        category=data["category"],

        unit_price=data["unit_price"],

        stock_qty=data["stock_qty"]

    )

    db.session.add(product)

    db.session.commit()

    return jsonify({

        "success": True,

        "message": "Product created"

    })
@product_bp.route(
    "/api/products",
    methods=["GET"]
)
def get_products():

    products = Product.query.all()

    data = []

    for product in products:

        data.append({

            "id": product.id,

            "name": product.name,

            "category": product.category,

            "unit_price": float(
                product.unit_price
            ),

            "stock_qty": product.stock_qty,

            "is_active": product.is_active

        })

    return jsonify({

        "success": True,

        "data": data

    })
@product_bp.route(
    "/api/products/<int:product_id>",
    methods=["PUT"]
)
def update_product(product_id):

    product = Product.query.get(
        product_id
    )

    if not product:

        return jsonify({

            "success": False,

            "message": "Product not found"

        }), 404

    data = request.json

    product.name = data.get(
        "name",
        product.name
    )

    product.category = data.get(
        "category",
        product.category
    )

    product.unit_price = data.get(
        "unit_price",
        product.unit_price
    )

    product.stock_qty = data.get(
        "stock_qty",
        product.stock_qty
    )

    db.session.commit()

    return jsonify({

        "success": True,

        "message": "Product updated"

    })
@product_bp.route(
    "/api/products/<int:product_id>",
    methods=["DELETE"]
)
def delete_product(product_id):

    product = Product.query.get(
        product_id
    )

    if not product:

        return jsonify({

            "success": False,

            "message": "Product not found"

        }), 404

    db.session.delete(product)

    db.session.commit()

    return jsonify({

        "success": True,

        "message": "Product deleted"

    })