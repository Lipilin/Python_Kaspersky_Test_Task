from datetime import date

from sqlalchemy.orm import Session

from kaspersky_python.database.Database import Database
from kaspersky_python.database.tables.Vulnerability import Vulnerability

from .Migration import Migration


class VulnerabilitiesMigration(Migration):
    def __init__(
        self,
        file_path: str,
        product_mapping: dict[tuple[str, str], int | None],
        version_mapping: dict[tuple[int, str], int | None],
    ) -> None:
        super().__init__(file_path)
        self.__product_mapping = product_mapping
        self.__version_mapping = version_mapping

    def save_data(self, batch: list) -> None:
        with Session(Database().engine) as session:
            vulnerabilities = []
            for data in batch:
                vendor = data.get("vendor")
                product_name = data.get("product")
                product_id = self.__product_mapping.get((vendor, product_name))
                fixed_version = data.get("fixed_version")
                fixed_version_id = self.__version_mapping.get((product_id, fixed_version))
                if fixed_version_id is None:
                    continue
                vulnerabilities.append(
                    Vulnerability(
                        product_id=product_id,
                        kla_id=data.get("KLA_id"),
                        description=data.get("description"),
                        publish_date=date.fromisoformat(data.get("publish_date")),
                        start_vuln_version=data.get("start_vuln_version"),
                        fixed_version_id=fixed_version_id,
                    )
                )
            session.add_all(vulnerabilities)
            session.commit()
        print(f"Сохранено {len(batch)} уязвимостей")
