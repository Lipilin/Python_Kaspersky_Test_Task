from sqlalchemy.orm import Session

from kaspersky_python.database.Database import Database
from kaspersky_python.database.tables.Product import Product
from kaspersky_python.database.tables.Vulnerability import Vulnerability


def get_product_by_name(session: Session, name: str) -> Product | None:
    return session.query(Product).filter_by(product_name=name).first()


def get_vulnerabilities_data(name: str, version: str) -> list[Vulnerability] | None:
    with Session(Database().engine, expire_on_commit=False) as session:
        product = get_product_by_name(session, name)
        if product is None:
            raise ValueError("Продукт не найден")
        vulnerabilities = [
            vulnerability
            for vulnerability in product.vulnerabilities
            if vulnerability.start_vuln_version <= version <= vulnerability.fixed_version
        ]
        if not vulnerabilities:
            return None
        return vulnerabilities


def get_last_stable_version(name: str) -> str | None:
    with Session(Database().engine, expire_on_commit=False) as session:
        product = get_product_by_name(session, name)
        if product is None:
            raise ValueError("Продукт не найден")
        if not product.vulnerabilities:
            return None
        return max(vulnerability.fixed_version for vulnerability in product.vulnerabilities)
