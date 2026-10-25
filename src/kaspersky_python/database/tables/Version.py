from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from kaspersky_python.database.base import Base

if TYPE_CHECKING:
    from kaspersky_python.database.tables.Product import Product


class Version(Base):
    __tablename__ = "versions"
    __table_args__ = (UniqueConstraint("product_id", "version"),)

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id", ondelete="CASCADE"), nullable=False)
    version: Mapped[str] = mapped_column(String(255), nullable=False)

    product: Mapped[Product] = relationship(back_populates="versions")
