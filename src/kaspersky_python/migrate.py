from .parser import parse
from .configs import VULNERABILITIES_DUMP, VERSIONS_DUMP
from .migrations import VersionsMigration, VulnerabilitiesMigration

def migrate() -> None:
    print("Начало миграции")
    try:
        print("Началась миграция версий")
        VersionsMigration(VERSIONS_DUMP).migrate()
        print("Началась миграция уязвимостей")
        VulnerabilitiesMigration(VULNERABILITIES_DUMP).migrate()
        print("Миграции завершены")
    except Exception as e:
        pass

if __name__ == "__main__":
    migrate()