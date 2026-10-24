import sys

from kaspersky_python.configs import read_env
from kaspersky_python.configs import VULNERABILITIES_DUMP, VERSIONS_DUMP
from kaspersky_python.database import Database
from kaspersky_python.migrations import VersionsMigration, VulnerabilitiesMigration


class Migrate:
    def migrate(self) -> None:
        print("Начало миграций")
        try:
            self.__initialize_database()
            self.__migrate_versions()
            self.__migrate_vulnerabilities()
        except Exception as e:
            print(f"Ошибка при миграции: {e}")
            sys.exit(1)
        print("Миграции завершена")

    def __initialize_database(self) -> None:
        print("Началось пересоздание базы данных")
        database = Database()
        database.create_database()
        database.reset_tables()
        database.create_tables()
        print("База данных пересоздана")

    def __migrate_versions(self) -> None:
        print("Началась миграция версий")
        VersionsMigration(VERSIONS_DUMP).migrate()
        print("Миграция версий завершена")

    def __migrate_vulnerabilities(self) -> None:
        print("Началась миграция уязвимостей")
        VulnerabilitiesMigration(VULNERABILITIES_DUMP).migrate()
        print("Миграция уязвимостей завершена")


def main() -> None:
    read_env()
    Migrate().migrate()


if __name__ == "__main__":
    main()
