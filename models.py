from __future__ import annotations

import enum
from database import Base
from sqlalchemy import Integer, String, Boolean, DateTime, Float, Column, ForeignKey, Float, Table, Column
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime

order_product = Table(
    "order_product",
    Base.metadata,
    Column("order_id", ForeignKey("orders.id"), primary_key=True),
    Column("product_id", ForeignKey("products.id"), primary_key=True)
)

class UserRole(str, enum.Enum):
    ADMIN = "admin"
    MODERATOR = "moderator"
    USER = "user"
    
    
class User(Base):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(255), nullable=False)
    role: Mapped[str] = mapped_column(String(20), default=UserRole.USER, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime)
    
    products: Mapped[list["Product"]] = relationship(
        "Product",
        back_populates="created_by"
    )

    orders: Mapped[list["Order"]] = relationship(
        "Order",
        back_populates="user"
    )
    
class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    price: Mapped[float] = mapped_column(Float, nullable=False)
    description: Mapped[str | None] = mapped_column(String(150), nullable=True)
    
    created_by_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable = True)
    created_by: Mapped["User"] = relationship(
        "User",
        back_populates="products"
    )

    orders: Mapped[list["Order"]] = relationship(
        "Order",
        secondary=order_product,
        back_populates="products"
    )
    
class Order(Base):
    __tablename__ = "orders"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    total_price: Mapped[float] = mapped_column(Float)
    created_at: Mapped[datetime] = mapped_column(DateTime)
    
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship(
        "User",
        back_populates="orders"
    )

    products: Mapped[list["Product"]] = relationship(
        "Product",
        secondary=order_product,
        back_populates="orders"
    )


# Base.metadata.create_all(engine)