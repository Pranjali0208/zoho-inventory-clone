from app.config.db import db
from datetime import datetime


class Invoice(db.Model):

    __tablename__ = "invoices"

    id = db.Column(db.Integer, primary_key=True)

    invoice_number = db.Column(
        db.String(20),
        unique=True,
        nullable=False
    )

    customer_id = db.Column(
        db.Integer,
        db.ForeignKey("customers.id")
    )

    issue_date = db.Column(db.Date, nullable=False)

    due_date = db.Column(db.Date, nullable=False)

    status = db.Column(
        db.String(20),
        default="draft"
    )

    vat_rate = db.Column(
        db.Numeric(5, 2),
        default=5.00
    )

    notes = db.Column(db.Text)

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )