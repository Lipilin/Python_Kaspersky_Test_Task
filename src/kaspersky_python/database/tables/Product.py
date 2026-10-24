from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from kaspersky_python.database.base import Base

if TYPE_CHECKING:
    from kaspersky_python.database.tables.Version import Version
    from kaspersky_python.database.tables.Vulnerability import Vulnerability


class Product(Base):
    __tablename__ = "products"
    __table_args__ = (UniqueConstraint("vendor", "product_name"),)

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    product_name: Mapped[str] = mapped_column(String(255), nullable=False)
    vendor: Mapped[str] = mapped_column(String(255), nullable=False)

    versions: Mapped[list[Version]] = relationship(back_populates="product")
    vulnerabilities: Mapped[list[Vulnerability]] = relationship(back_populates="product")
