from app.config.db import db


class Product(db.Model):

    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(150), nullable=False)

    category = db.Column(db.String(50))

    unit_price = db.Column(db.Numeric(10, 3), nullable=False)

    stock_qty = db.Column(db.Integer, default=0)

    is_active = db.Column(db.Boolean, default=True)