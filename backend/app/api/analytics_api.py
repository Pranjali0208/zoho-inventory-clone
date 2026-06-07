from flask import Blueprint, jsonify

from app.models.product_model import Product
from app.models.invoice_item_model import InvoiceItem
from app.models.customer_model import Customer
from app.models.invoice_model import Invoice

analytics_bp = Blueprint(
    "analytics",
    __name__
)


@analytics_bp.route(
    "/api/analytics/top-products",
    methods=["GET"]
)
def top_products():

    items = InvoiceItem.query.all()

    product_sales = {}

    for item in items:

        if item.product_id not in product_sales:

            product_sales[item.product_id] = 0

        product_sales[item.product_id] += item.quantity

    all_products = Product.query.all()

    product_map = {}

    for product in all_products:

        product_map[product.id] = product

    result = []

    for product_id, quantity in product_sales.items():

        product = product_map.get(product_id)

        if product:

            result.append({

                "product_id": product.id,

                "product_name": product.name,

                "quantity_sold": quantity

            })

    result.sort(
        key=lambda x: x["quantity_sold"],
        reverse=True
    )

    return jsonify({

        "success": True,

        "data": result

    })
@analytics_bp.route(
    "/api/analytics/low-stock",
    methods=["GET"]
)
def low_stock():

    products = Product.query.filter(
        Product.stock_qty < 20
    ).all()

    data = []

    for product in products:

        data.append({

            "id": product.id,

            "name": product.name,

            "stock_qty": product.stock_qty,

            "category": product.category

        })

    return jsonify({

        "success": True,

        "count": len(data),

        "data": data

    })
@analytics_bp.route(
    "/api/analytics/revenue",
    methods=["GET"]
)
def revenue():

    items = InvoiceItem.query.all()

    total_revenue = 0

    for item in items:

        total_revenue += (

            item.quantity *

            float(item.unit_price)

        )

    total_revenue = round(
        total_revenue,
        3
    )

    return jsonify({

        "success": True,

        "total_revenue":
            total_revenue

    })

@analytics_bp.route(
    "/api/analytics/top-customers",
    methods=["GET"]
)
def top_customers():

    invoices = Invoice.query.all()

    customer_counts = {}

    for invoice in invoices:

        if invoice.customer_id not in customer_counts:

            customer_counts[
                invoice.customer_id
            ] = 0

        customer_counts[
            invoice.customer_id
        ] += 1

    customers = Customer.query.all()

    customer_map = {}

    for customer in customers:

        customer_map[
            customer.id
        ] = customer

    result = []

    for customer_id, count in customer_counts.items():

        customer = customer_map.get(
            customer_id
        )

        result.append({

            "customer":
                customer.name,

            "invoice_count":
                count

        })

    result.sort(

        key=lambda x: x[
            "invoice_count"
        ],

        reverse=True

    )

    return jsonify({

        "success": True,

        "data": result

    })