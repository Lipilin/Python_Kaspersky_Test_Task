import sys

from sqlalchemy.exc import SQLAlchemyError

from kaspersky_python.utils.MigrationController import MigrationController


class MigrationConsole:
    def migrate(self) -> None:
        print("Начало миграций")
        try:
            migration_controller = MigrationController()
            self.__initialize_database(migration_controller)
            self.__migrate_products(migration_controller)
            self.__migrate_versions(migration_controller)
            self.__migrate_vulnerabilities(migration_controller)
        except (OSError, ValueError, FileNotFoundError, SQLAlchemyError) as e:
            print(f"Ошибка при миграции: {e}")
            sys.exit(1)
        print("Миграции завершена")

    def __initialize_database(self, migration_controller: MigrationController) -> None:
        print("Началось пересоздание базы данных")
        migration_controller.initialize_database()
        print("База данных пересоздана")

    def __migrate_products(self, migration_controller: MigrationController) -> None:
        print("Началась миграция продуктов")
        migration_controller.migrate_products()
        print("Миграция продуктов завершена")

    def __migrate_versions(self, migration_controller: MigrationController) -> None:
        print("Началась миграция версий")
        migration_controller.migrate_versions()
        print("Миграция версий завершена")

    def __migrate_vulnerabilities(
        self, migration_controller: MigrationController
    ) -> None:
        print("Началась миграция уязвимостей")
        migration_controller.migrate_vulnerabilities()
        print("Миграция уязвимостей завершена")
