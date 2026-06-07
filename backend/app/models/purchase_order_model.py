from app.config.db import db
from datetime import datetime


class PurchaseOrder(db.Model):

    __tablename__ = "purchase_orders"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    po_number = db.Column(
        db.String(50),
        unique=True,
        nullable=False
    )

    supplier_id = db.Column(
        db.Integer,
        db.ForeignKey("suppliers.id"),
        nullable=False
    )

    order_date = db.Column(
        db.Date,
        nullable=False
    )

    status = db.Column(
        db.String(20),
        default="pending"
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )