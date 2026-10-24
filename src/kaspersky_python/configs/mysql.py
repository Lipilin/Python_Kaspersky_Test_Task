import os

from sqlalchemy.engine import URL

from .config import ENV_ERROR_MESSAGE


def mysql_url(*, with_database: bool = True) -> str:
    values: dict[str, str] = {}
    for key, error_message in ENV_ERROR_MESSAGE.items():
        if not with_database and key == "MYSQL_DATABASE":
            continue
        env_value = os.getenv(key)
        if not env_value:
            raise ValueError(error_message)
        values[key] = env_value

    return URL.create(
        drivername="mysql+pymysql",
        username=values["MYSQL_USER"],
        password=values["MYSQL_PASSWORD"],
        host=values["MYSQL_HOST"],
        port=int(values["MYSQL_PORT"]),
        database=values["MYSQL_DATABASE"] if with_database else None,
    ).render_as_string(hide_password=False)
