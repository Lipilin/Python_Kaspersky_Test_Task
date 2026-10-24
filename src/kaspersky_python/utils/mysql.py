import os

from sqlalchemy.engine import URL

from kaspersky_python.configs.env import (
    MYSQL_DATABASE,
    MYSQL_HOST,
    MYSQL_PASSWORD,
    MYSQL_PORT,
    MYSQL_USER,
)


def mysql_url(with_database: bool = True) -> URL:
    return URL.create(
        drivername="mysql+pymysql",
        username=os.getenv(MYSQL_USER),
        password=os.getenv(MYSQL_PASSWORD),
        host=os.getenv(MYSQL_HOST),
        port=int(os.getenv(MYSQL_PORT)),
        database=os.getenv(MYSQL_DATABASE) if with_database else None,
    )
