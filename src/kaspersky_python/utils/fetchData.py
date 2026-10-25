from sqlalchemy.orm import Session

from kaspersky_python.database.Database import Database
from kaspersky_python.database.tables.Product import Product
from kaspersky_python.database.tables.Vulnerability import Vulnerability
from kaspersky_python.utils.version_compare import compare_versions, parse_version


def get_product_by_name(session: Session, name: str) -> Product | None:
    return session.query(Product).filter_by(product_name=name).first()


def get_vulnerabilities_data(name: str, version: str) -> list[Vulnerability] | None:
    with Session(Database().engine, expire_on_commit=False) as session:
        product = get_product_by_name(session, name)
        if product is None:
            raise ValueError("Переданный продукт не найден")
        product_versions = {product_version.version for product_version in product.versions}
        if version not in product_versions:
            raise ValueError("Переданная версия не найдена")
        vulnerabilities = [
            vulnerability
            for vulnerability in product.vulnerabilities
            if compare_versions(vulnerability.start_vuln_version, version) <= 0
            and compare_versions(version, vulnerability.fixed_version) <= 0
        ]
        if not vulnerabilities:
            return None
        return vulnerabilities


def get_last_stable_version(name: str) -> str | None:
    with Session(Database().engine, expire_on_commit=False) as session:
        product = get_product_by_name(session, name)
        if product is None:
            raise ValueError("Переданный продукт не найден")
        versions = [product_version.version for product_version in product.versions]
        versions.extend(vulnerability.fixed_version for vulnerability in product.vulnerabilities)
        if not versions:
            return None
        return max(versions, key=parse_version)
