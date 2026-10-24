import ijson


def parse(file_path: str):
    with open(file_path, "rb") as file:
        yield from ijson.items(file, "item")
