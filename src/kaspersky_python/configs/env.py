from dotenv import load_dotenv
import os
import sys

MYSQL_USER = "MYSQL_USER"
MYSQL_PASSWORD = "MYSQL_PASSWORD"
MYSQL_DATABASE = "MYSQL_DATABASE"
MYSQL_HOST = "MYSQL_HOST"
MYSQL_PORT = "MYSQL_PORT"
MYSQL_URL = "MYSQL_URL"

ENV_ERROR_MESSAGE = {
    MYSQL_USER: f"{MYSQL_USER} не найден",
    MYSQL_PASSWORD: f"{MYSQL_PASSWORD} не найден",
    MYSQL_DATABASE: f"{MYSQL_DATABASE} не найден",
    MYSQL_HOST: f"{MYSQL_HOST} не найден",
    MYSQL_PORT: f"{MYSQL_PORT} не найден",
}


def read_env() -> None:
    try:
        if not load_dotenv():
            raise FileNotFoundError(".env файл не был найден")
        for key, value in ENV_ERROR_MESSAGE.items():
            if not os.getenv(key):
                raise ValueError(value)
    except Exception as e:
        print(f"Возникла ошибка: {e}")
        sys.exit(1)
