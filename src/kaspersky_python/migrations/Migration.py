from abc import ABC, abstractmethod
from kaspersky_python.configs.config import BATCHING_SIZE
from kaspersky_python.parser import parse

class Migration(ABC):

    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    def get_data(self):
        batch = []
        while(data := parse(self.file_path)):
            batch.append(data)
            if len(batch) == BATCHING_SIZE:
                migrate(batch)

    @abstractmethod
    def migrate(self) -> None:
        pass