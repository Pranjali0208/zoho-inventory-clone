from flask import Blueprint, jsonify

from app.models.product_model import Product
from app.models.invoice_model import Invoice
from app.models.customer_model import Customer

from app.models.purchase_order_model import PurchaseOrder
from app.models.supplier_model import Supplier
from app.models.invoice_item_model import InvoiceItem

dashboard_bp = Blueprint(
    "dashboard",
    __name__
)


@dashboard_bp.route(
    "/api/dashboard/summary",
    methods=["GET"]
)
def dashboard_summary():

    total_invoices = Invoice.query.count()

    paid_invoices = Invoice.query.filter_by(
        status="paid"
    ).count()

    draft_invoices = Invoice.query.filter_by(
        status="draft"
    ).count()

    overdue_invoices = Invoice.query.filter_by(
        status="overdue"
    ).count()

    items = InvoiceItem.query.all()

    total_revenue = 0

    for item in items:

        line_total = (
            item.quantity *
            float(item.unit_price)
        )

        total_revenue += line_total

    total_revenue = round(
        total_revenue,
        3
    )

    return jsonify({

        "success": True,

        "total_invoices":
            total_invoices,

        "paid_invoices":
            paid_invoices,

        "draft_invoices":
            draft_invoices,

        "overdue_invoices":
            overdue_invoices,

        "total_revenue":
            total_revenue

    })


@dashboard_bp.route(
    "/api/dashboard/monthly-sales",
    methods=["GET"]
)
def monthly_sales():

    invoices = Invoice.query.all()

    monthly_data = {}

    for invoice in invoices:

        month = invoice.issue_date.strftime(
            "%b"
        )

        items = InvoiceItem.query.filter_by(
            invoice_id=invoice.id
        ).all()

        invoice_total = 0

        for item in items:

            line_total = (
                item.quantity *
                float(item.unit_price)
            )

            invoice_total += line_total

        if month not in monthly_data:

            monthly_data[month] = 0

        monthly_data[month] += invoice_total

    months = []

    sales = []

    for month, total in monthly_data.items():

        months.append(month)

        sales.append(
            round(total, 3)
        )

    return jsonify({

        "success": True,

        "months": months,

        "sales": sales

    })

@dashboard_bp.route(
    "/api/dashboard/low-stock",
    methods=["GET"]
)
def low_stock_products():

    products = Product.query.all()

    data = []

    for product in products:

        if product.stock_qty < 10:

            data.append({

                "id": product.id,

                "name": product.name,

                "stock_qty": product.stock_qty

            })

    return jsonify({

        "success": True,

        "data": data

    })

@dashboard_bp.route(
    "/api/dashboard/recent-activities",
    methods=["GET"]
)
def get_recent_activities():

    invoices = Invoice.query.order_by(
        Invoice.id.desc()
    ).limit(5).all()

    purchase_orders = PurchaseOrder.query.order_by(
        PurchaseOrder.id.desc()
    ).limit(5).all()

    recent_invoices = []

    for invoice in invoices:

        customer = Customer.query.get(
            invoice.customer_id
        )

        recent_invoices.append({

            "invoice_number":
            invoice.invoice_number,

            "customer":
            customer.name,

            "status":
            invoice.status

        })

    recent_purchase_orders = []

    for po in purchase_orders:

        supplier = Supplier.query.get(
            po.supplier_id
        )

        recent_purchase_orders.append({

            "po_number":
            po.po_number,

            "supplier":
            supplier.name,

            "status":
            po.status

        })

    return jsonify({

        "recent_invoices":
        recent_invoices,

        "recent_purchase_orders":
        recent_purchase_orders

    })