from dotenv import load_dotenv
import os
import sys

from .config import ENV_ERROR_MESSAGE

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
