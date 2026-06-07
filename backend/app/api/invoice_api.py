from flask import Blueprint, jsonify

from app.models.invoice_model import Invoice
from app.models.invoice_item_model import InvoiceItem
from app.models.customer_model import Customer
from app.models.product_model import Product


invoice_bp = Blueprint(
    "invoice",
    __name__
)


@invoice_bp.route(
    "/api/invoices/<int:invoice_id>/summary",
    methods=["GET"]
)
def get_invoice_summary(invoice_id):

    # GET INVOICE
    invoice = Invoice.query.get(invoice_id)

    if not invoice:

        return jsonify({

            "success": False,

            "message": "Invoice not found"

        }), 404

    # GET CUSTOMER
    customer = Customer.query.get(
        invoice.customer_id
    )

    # GET ITEMS
    items = InvoiceItem.query.filter_by(
        invoice_id=invoice_id
    ).all()

    # GET PRODUCTS ONCE
    all_products = Product.query.all()

    # PRODUCT MAP
    product_map = {}

    for product in all_products:

        product_map[product.id] = product

    line_items = []

    subtotal = 0

    # CALCULATIONS
    for item in items:

        product = product_map.get(
            item.product_id
        )

        line_total = (
            item.quantity *
            float(item.unit_price)
        )

        line_total = round(
            line_total,
            3
        )

        subtotal += line_total

        line_items.append({

            "product": product.name,

            "quantity": item.quantity,

            "unit_price": round(
                float(item.unit_price),
                3
            ),

            "line_total": line_total

        })

    subtotal = round(subtotal, 3)

    vat_rate = float(invoice.vat_rate)

    vat_amount = round(
        subtotal * (vat_rate / 100),
        3
    )

    grand_total = round(
        subtotal + vat_amount,
        3
    )

    return jsonify({

        "invoice_number": invoice.invoice_number,

        "customer": customer.name,

        "line_items": line_items,

        "subtotal": subtotal,

        "vat_rate": vat_rate,

        "vat_amount": vat_amount,

        "grand_total": grand_total,

        "currency": "OMR"

    })

from flask import request
from datetime import datetime
from app.config.db import db


@invoice_bp.route(
    "/api/invoices/create",
    methods=["POST"]
)
def create_invoice():

    data = request.json

    customer_id = data.get(
        "customer_id"
    )

    items = data.get(
        "items",
        []
    )

    notes = data.get(
        "notes"
    )

    # VALIDATION
    if not customer_id:

        return jsonify({

            "success": False,

            "message": "Customer is required"

        }), 400

    if len(items) == 0:

        return jsonify({

            "success": False,

            "message": "Invoice items required"

        }), 400

    # CREATE INVOICE
    invoice = Invoice(

        invoice_number=f"INV-{int(datetime.now().timestamp())}",

        customer_id=customer_id,

        issue_date=datetime.now().date(),

        due_date=datetime.now().date(),

        status="draft",

        vat_rate=5.00,

        notes=notes

    )

    db.session.add(invoice)

    db.session.commit()

    # GET PRODUCTS
    all_products = Product.query.all()

    product_map = {}

    for product in all_products:

        product_map[product.id] = product

    subtotal = 0

    # CREATE ITEMS
    for item in items:

        product = product_map.get(
            item["product_id"]
        )

        if not product:

            continue

        quantity = item["quantity"]

        unit_price = float(
            product.unit_price
        )

        line_total = (
            quantity * unit_price
        )

        subtotal += line_total

        invoice_item = InvoiceItem(

            invoice_id=invoice.id,

            product_id=product.id,

            quantity=quantity,

            unit_price=unit_price

        )

        db.session.add(invoice_item)

    db.session.commit()

    subtotal = round(
        subtotal,
        3
    )

    vat_amount = round(
        subtotal * 0.05,
        3
    )

    grand_total = round(
        subtotal + vat_amount,
        3
    )

    return jsonify({

        "success": True,

        "message": "Invoice created successfully",

        "invoice_id": invoice.id,

        "subtotal": subtotal,

        "vat_amount": vat_amount,

        "grand_total": grand_total

    })

@invoice_bp.route(
    "/api/invoices",
    methods=["GET"]
)
def get_all_invoices():
    status=request.args.get("status")
    search=request.args.get("search")
    query=Invoice.query
    if status:
         query = query.filter_by(
            status=status
        )
    
    if search:
        query=query.filter(
            Invoice.invoice_number.ilike(f"%{search}%")
        )

    # invoices = query.all()
    page=request.args.get("page",1,type=int)
    limit=request.args.get("limit",5,type=int)
    pagination=query.paginate(page=page,per_page=limit,error_out=False)
    invoices=pagination.items
    customer_ids = []

    for invoice in invoices:

        customer_ids.append(
            invoice.customer_id
        )

    customers = Customer.query.filter(
        Customer.id.in_(customer_ids)
    ).all()

    customer_map = {}

    for customer in customers:

        customer_map[customer.id] = customer

    invoice_list = []

    for invoice in invoices:

        customer = customer_map.get(
            invoice.customer_id
        )

        invoice_list.append({

            "id": invoice.id,

            "invoice_number": invoice.invoice_number,

            "customer": customer.name if customer else None,

            "status": invoice.status,

            "issue_date": str(
                invoice.issue_date
            ),

            "due_date": str(
                invoice.due_date
            ),

            "vat_rate": float(
                invoice.vat_rate
            )

        })

    return jsonify({

        "success": True,

        "count": len(invoice_list),

        "data": invoice_list

    })