from kaspersky_python.configs import read_env
from kaspersky_python.console.MigrationConsole import MigrationConsole


def main() -> None:
    read_env()
    migration_controller = MigrationConsole()    
    migration_controller.migrate()


if __name__ == "__main__":
    main()
