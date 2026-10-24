from __future__ import annotations

from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine, make_url

from kaspersky_python.configs.mysql import mysql_url
from kaspersky_python.database.base import Base
from kaspersky_python.database.tables import Product, Version, Vulnerability  # noqa: F401


class Database:
    _instance: Database | None = None

    def __new__(cls) -> Database:
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._url = mysql_url(with_database=True)
            cls._instance._server_url = mysql_url(with_database=False)
            cls._instance._engine = create_engine(cls._instance._url)
        return cls._instance

    @property
    def url(self) -> str:
        return self._url

    @property
    def server_url(self) -> str:
        return self._server_url

    @property
    def engine(self) -> Engine:
        return self._engine

    def create_database(self) -> None:
        database_name = make_url(self._url).database
        if not database_name:
            raise ValueError("MYSQL_DATABASE не найден")

        server_engine = create_engine(self._server_url)
        try:
            with server_engine.connect() as connection:
                connection.execute(
                    text(
                        f"CREATE DATABASE IF NOT EXISTS `{database_name}` "
                        "CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci"
                    )
                )
                connection.commit()
        finally:
            server_engine.dispose()

    def create_tables(self) -> None:
        Base.metadata.create_all(self._engine)

    def reset_tables(self) -> None:
        Base.metadata.drop_all(self._engine)
