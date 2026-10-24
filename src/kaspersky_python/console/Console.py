import sys

class Console:
    def __init__(self) -> None:
        pass


    def print_menu(self) -> None:
        print("1. Вывести информацию о версии без уязвимостей")
        print("2. Вывести информацию об уязвимостях продукта ")
        print("0. Выйти")
    
    def run(self) -> None:
        while True:
            self.print_menu()
            try:
                command = int(input())
            except Exception as e:
                print("Некорректный ввод")
                continue
            match command:
                case 1:
                    continue
                case 2:
                    continue
                case 0:
                    sys.exit(0)
                case _:
                    print("Команда не распознана")
                    continue