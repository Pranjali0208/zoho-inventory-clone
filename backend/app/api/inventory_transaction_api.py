from flask import (
    Blueprint,
    jsonify
)

from app.models.inventory_transaction_model import (
    InventoryTransaction
)

from app.models.product_model import Product

inventory_transaction_bp = Blueprint(
    "inventory_transaction",
    __name__
)


@inventory_transaction_bp.route(
    "/api/inventory-transactions",
    methods=["GET"]
)
def get_inventory_transactions():

    transactions = InventoryTransaction.query.all()

    product_ids = []

    for transaction in transactions:

        product_ids.append(
            transaction.product_id
        )

    products = Product.query.filter(
        Product.id.in_(product_ids)
    ).all()

    product_map = {}

    for product in products:

        product_map[product.id] = product

    data = []

    for transaction in transactions:

        product = product_map.get(
            transaction.product_id
        )

        data.append({

            "id":
                transaction.id,

            "product":
                product.name if product else None,

            "transaction_type":
                transaction.transaction_type,

            "quantity":
                transaction.quantity,

            "remarks":
                transaction.remarks,

            "created_at":
                str(transaction.created_at)

        })

    return jsonify({

        "success": True,

        "count":
            len(data),

        "data":
            data

    })