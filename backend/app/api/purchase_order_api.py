from flask import (
    Blueprint,
    request,
    jsonify
)

from datetime import datetime

from app.config.db import db

from app.models.supplier_model import Supplier
from app.models.product_model import Product

from app.models.purchase_order_model import PurchaseOrder
from app.models.purchase_order_item_model import PurchaseOrderItem

from app.models.inventory_transaction_model import (
    InventoryTransaction
)

from app.utils.auth import (
    requires_auth
)

purchase_order_bp = Blueprint(
    "purchase_order",
    __name__
)


@purchase_order_bp.route(
    "/api/purchase-orders",
    methods=["POST"]
)
@requires_auth
def create_purchase_order():

    data = request.json

    supplier_id = data.get(
        "supplier_id"
    )

    items = data.get(
        "items",
        []
    )

    supplier = Supplier.query.get(
        supplier_id
    )

    if not supplier:

        return jsonify({

            "success": False,

            "message": "Supplier not found"

        }), 404

    po = PurchaseOrder(

        po_number=f"PO-{int(datetime.now().timestamp())}",

        supplier_id=supplier_id,

        order_date=datetime.now().date(),

        status="pending"

    )

    db.session.add(po)

    db.session.commit()

    for item in items:

        product = Product.query.get(
            item["product_id"]
        )

        if not product:
            continue

        po_item = PurchaseOrderItem(

            purchase_order_id=po.id,

            product_id=product.id,

            quantity=item["quantity"],

            unit_price=product.unit_price

        )

        db.session.add(po_item)

    db.session.commit()

    return jsonify({

        "success": True,

        "message": "Purchase Order Created",

        "purchase_order_id": po.id

    })


@purchase_order_bp.route(
    "/api/purchase-orders/<int:po_id>/receive",
    methods=["POST"]
)
@requires_auth
def receive_purchase_order(po_id):

    po = PurchaseOrder.query.get(
        po_id
    )

    if not po:

        return jsonify({

            "success": False,

            "message": "Purchase Order not found"

        }), 404

    items = PurchaseOrderItem.query.filter_by(
        purchase_order_id=po.id
    ).all()

    product_ids = []

    for item in items:

        product_ids.append(
            item.product_id
        )

    products = Product.query.filter(
        Product.id.in_(product_ids)
    ).all()

    product_map = {}

    for product in products:

        product_map[
            product.id
        ] = product

    for item in items:

        product = product_map.get(
            item.product_id
        )

        if product:

            product.stock_qty += (
                item.quantity
            )

            transaction = InventoryTransaction(

                product_id=product.id,

                transaction_type="PURCHASE",

                quantity=item.quantity,

                remarks=f"PO #{po.id}"

            )

            db.session.add(
                transaction
            )

    po.status = "received"

    db.session.commit()

    return jsonify({

        "success": True,

        "message":
        "Stock updated successfully"

    })


@purchase_order_bp.route(
    "/api/purchase-orders",
    methods=["GET"]
)
@requires_auth
def get_purchase_orders():

    purchase_orders = (
        PurchaseOrder.query.all()
    )

    data = []

    for po in purchase_orders:

        supplier = Supplier.query.get(
            po.supplier_id
        )

        data.append({

            "id": po.id,

            "po_number":
            po.po_number,

            "supplier":
            supplier.name,

            "order_date":
            str(po.order_date),

            "status":
            po.status

        })

    return jsonify({

        "success": True,

        "count": len(data),

        "data": data

    })


@purchase_order_bp.route(
    "/api/purchase-orders/<int:po_id>",
    methods=["GET"]
)
@requires_auth
def get_purchase_order_details(
    po_id
):

    po = PurchaseOrder.query.get(
        po_id
    )

    if not po:

        return jsonify({

            "success": False,

            "message":
            "Purchase Order not found"

        }), 404

    supplier = Supplier.query.get(
        po.supplier_id
    )

    items = PurchaseOrderItem.query.filter_by(
        purchase_order_id=po.id
    ).all()

    line_items = []

    subtotal = 0

    for item in items:

        product = Product.query.get(
            item.product_id
        )

        line_total = (

            item.quantity *

            float(
                item.unit_price
            )

        )

        subtotal += line_total

        line_items.append({

            "product":
            product.name,

            "quantity":
            item.quantity,

            "unit_price":
            float(
                item.unit_price
            ),

            "line_total":
            round(
                line_total,
                3
            )

        })

    return jsonify({

        "success": True,

        "data": {

            "po_number":
            po.po_number,

            "supplier":
            supplier.name,

            "order_date":
            str(
                po.order_date
            ),

            "status":
            po.status,

            "subtotal":
            round(
                subtotal,
                3
            ),

            "items":
            line_items

        }

    })