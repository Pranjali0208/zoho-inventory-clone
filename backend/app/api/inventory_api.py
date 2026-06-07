from flask import Blueprint, jsonify
from app.models.product_model import Product

inventory_bp = Blueprint(
    "inventory",
    __name__
)

@inventory_bp.route(
    "/api/inventory",
    methods=["GET"]
)
def get_inventory():

    products = Product.query.all()

    data = []

    for product in products:

        data.append({

            "id": product.id,

            "product_name": product.name,

            "category": product.category,

            "stock_qty": product.stock_qty,

            "unit_price": float(
                product.unit_price
            ),

            "status":
                "Low Stock"
                if product.stock_qty < 10
                else "In Stock"

        })

    return jsonify({

        "success": True,

        "data": data

    })