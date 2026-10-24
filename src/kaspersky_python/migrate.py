from kaspersky_python.configs import read_env
from kaspersky_python.utils.MigrationController import MigrationController


def main() -> None:
    read_env()
    migration_controller = MigrationController()    
    migration_controller.migrate()


if __name__ == "__main__":
    main()
