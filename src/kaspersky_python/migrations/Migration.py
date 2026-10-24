from abc import ABC, abstractmethod
from kaspersky_python.configs import BATCHING_SIZE
from kaspersky_python.parser import parse

class Migration(ABC):

    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    def migrate(self):
        batch = []
        for data in parse(self.file_path):
            batch.append(data)
            if len(batch) == BATCHING_SIZE:
                self.save_data(batch)
                batch = []
        if batch:
            self.save_data(batch)

    @abstractmethod
    def save_data(self, batch: list) -> None:
        raise NotImplementedError("Метод migrate должен быть реализован в классе-наследнике")