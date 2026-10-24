from .Migration import Migration

class VulnerabilitiesMigration(Migration):
    def __init__(self, file_path: str) -> None:
        super().__init__(file_path)

    def save_data(self, batch: list) -> None:
        print(f'Сохранено {len(batch)} уязвимостей')