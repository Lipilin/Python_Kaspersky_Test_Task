from .parser import parse
from .configs.dumps import VULNERABILITIES_DUMP, VERSIONS_DUMP
from .migrations import VersionsMigration, VulnerabilitiesMigration

def migrate() -> None:
    print("Начало миграции")
    try:
        
    except Exception as e:
        pass

if __name__ == "__main__":
    migrate()