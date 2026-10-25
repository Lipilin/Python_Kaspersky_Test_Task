from .Migration import Migration
from kaspersky_python.database.Database import Database
from kaspersky_python.database.tables.Version import Version
from sqlalchemy.orm import Session

class VersionsMigration(Migration):
    def __init__(
        self, 
        file_path: str, product_mapping: dict[tuple[str, str], int | None], 
        version_mapping: dict[tuple[int, str], int | None]
    ) -> None:
        super().__init__(file_path)
        self.__product_mapping = product_mapping
        self.__version_mapping = version_mapping

    def save_data(self, batch: list) -> None:
        with Session(Database().engine) as session:
            versions = []
            for data in batch:
                vendor = data.get('vendor')
                version = data.get('version')
                product_name = data.get('product')
                product_id = self.__product_mapping.get((vendor, product_name))
                if (product_id, version) in self.__version_mapping:
                    continue
                version = Version(
                    product_id=product_id,
                    version=version,
                )
                self.__version_mapping[(product_id, version)] = None
                versions.append(version)
            session.add_all(versions)
            session.commit()
            for version in versions:
                self.__version_mapping[(version.product_id, version.version)] = version.id
        print(f'Сохранено {len(batch)} версий')