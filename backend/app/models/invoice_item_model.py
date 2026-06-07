from app.config.db import db


class InvoiceItem(db.Model):

    __tablename__ = "invoice_items"

    id = db.Column(db.Integer, primary_key=True)

    invoice_id = db.Column(
        db.Integer,
        db.ForeignKey("invoices.id")
    )

    product_id = db.Column(
        db.Integer,
        db.ForeignKey("products.id")
    )

    quantity = db.Column(db.Integer, nullable=False)

    unit_price = db.Column(
        db.Numeric(10, 3),
        nullable=False
    )