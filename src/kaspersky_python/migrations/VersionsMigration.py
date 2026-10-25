from sqlalchemy.orm import Session

from kaspersky_python.database.Database import Database
from kaspersky_python.database.tables.Version import Version

from .Migration import Migration


class VersionsMigration(Migration):
    def __init__(
        self,
        file_path: str,
        product_mapping: dict[tuple[str, str], int | None],
    ) -> None:
        super().__init__(file_path)
        self.__product_mapping = product_mapping
        self.__loaded_versions: set[tuple[int | None, str]] = set()

    def save_data(self, batch: list) -> None:
        with Session(Database().engine) as session:
            versions = []
            for data in batch:
                vendor = data.get("vendor")
                product_name = data.get("product")
                version_value = data.get("version")
                product_id = self.__product_mapping.get((vendor, product_name))
                version_key = (product_id, version_value)
                if version_key in self.__loaded_versions:
                    continue
                self.__loaded_versions.add(version_key)
                versions.append(
                    Version(
                        product_id=product_id,
                        version=version_value,
                    )
                )
            session.add_all(versions)
            session.commit()
        print(f"Сохранено {len(batch)} версий")
