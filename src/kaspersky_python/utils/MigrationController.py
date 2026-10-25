from kaspersky_python.configs import VERSIONS_DUMP, VULNERABILITIES_DUMP
from kaspersky_python.database import Database
from kaspersky_python.migrations import VersionsMigration, VulnerabilitiesMigration
from kaspersky_python.migrations.ProductMigration import ProductMigration


class MigrationController:
    def __init__(self) -> None:
        self.__product_mapping: dict[tuple[str, str], int | None] = {}

    def migrate(self) -> None:
        self.initialize_database()
        self.migrate_products()
        self.migrate_versions()
        self.migrate_vulnerabilities()

    def initialize_database(self) -> None:
        database = Database()
        database.create_database()
        database.reset_tables()
        database.create_tables()

    def migrate_products(self) -> None:
        ProductMigration(VULNERABILITIES_DUMP, self.__product_mapping).migrate()

    def migrate_versions(self) -> None:
        VersionsMigration(VERSIONS_DUMP, self.__product_mapping).migrate()

    def migrate_vulnerabilities(self) -> None:
        VulnerabilitiesMigration(VULNERABILITIES_DUMP, self.__product_mapping).migrate()
