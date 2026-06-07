from app.config.db import db
from datetime import datetime


class InventoryTransaction(db.Model):

    __tablename__ = "inventory_transactions"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    product_id = db.Column(
        db.Integer,
        db.ForeignKey("products.id")
    )

    transaction_type = db.Column(
        db.String(20)
    )

    quantity = db.Column(
        db.Integer
    )

    remarks = db.Column(
        db.String(255)
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )