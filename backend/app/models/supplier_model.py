from app.config.db import db

class Supplier(db.Model):

    __tablename__ = "suppliers"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    name = db.Column(
        db.String(100),
        nullable=False
    )

    email = db.Column(
        db.String(100),
        unique=True
    )

    phone = db.Column(
        db.String(20)
    )

    country = db.Column(
        db.String(50)
    )