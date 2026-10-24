from .Migration import Migration

class VulnerabilitiesMigration(Migration):
    def __init__(self, file_path: str) -> None:
        super().__init__(file_path)

    def migrate(self) -> None:
        pass