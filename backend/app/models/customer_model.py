from app.config.db import db
from datetime import datetime


class Customer(db.Model):

    __tablename__ = "customers"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)

    email = db.Column(db.String(100), unique=True, nullable=False)

    phone = db.Column(db.String(20))

    country = db.Column(db.String(50), default="Oman")

    created_at = db.Column(db.DateTime, default=datetime.utcnow)