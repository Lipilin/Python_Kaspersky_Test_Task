import sys

from kaspersky_python.utils.fetchData import (
    get_last_stable_version,
    get_vulnerabilities_data,
)
from kaspersky_python.utils.formatOutput import (
    format_last_stable_version,
    format_vulnerabilities_data,
)


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
            except ValueError:
                print("Некорректный ввод")
                continue
            match command:
                case 1:
                    self.__print_last_stable_version()
                case 2:
                    self.__print_vulnerabilities_data()
                case 0:
                    sys.exit(0)
                case _:
                    print("Команда не распознана")
                    continue

    def __print_last_stable_version(self) -> None:
        name = input("Введите имя продукта: ")
        try:
            version = get_last_stable_version(name)
        except ValueError as error:
            print(error)
            return
        if version is None:
            print("Соответствующая стабильная версия не найдена")
            return
        format_last_stable_version(version)

    def __print_vulnerabilities_data(self) -> None:
        name = input("Введите имя продукта: ")
        version = input("Введите версию: ")
        try:
            vulnerabilities = get_vulnerabilities_data(name, version)
        except ValueError as error:
            print(error)
            return
        if vulnerabilities is None:
            print("Соответствующие уязвимости не найдены")
            return
        format_vulnerabilities_data(vulnerabilities)
