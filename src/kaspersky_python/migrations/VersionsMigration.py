from .Migration import Migration

class VersionsMigration(Migration):
    def __init__(self, file_path: str) -> None:
        super().__init__(file_path)

    def save_data(self, batch: list) -> None:
        print(f'Сохранено {len(batch)} версий')