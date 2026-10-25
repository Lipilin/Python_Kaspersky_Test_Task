# kaspersky-python

Консольное приложение для работы с данными о продуктах, версиях и уязвимостях. Требуется Python **3.12+** и менеджер зависимостей [uv].

## Установка uv

Если `uv` ещё не установлен

**Через pip**:

```bash
pip install uv
```

Проверка:

```bash
uv --version
```

## Запуск

### 1. Клонирование и зависимости

Из корня репозитория установите зависимости:

```bash
uv sync
```

### 2. Файл окружения `.env`

Скопируйте шаблон и отредактируйте значения под своё окружение.

**Linux / macOS:**

```bash
cp .env.example .env
```

**Windows (cmd):**

```cmd
copy .env.example .env
```

**Windows (PowerShell):**

```powershell
Copy-Item .env.example .env
```

Переменные в `.env`:

| Переменная | Назначение |
|------------|------------|
| `MYSQL_USER` | Пользователь MySQL для приложения |
| `MYSQL_PASSWORD` | Пароль этого пользователя |
| `MYSQL_DATABASE` | Имя базы данных |
| `MYSQL_HOST` | Хост (`localhost` для Docker и локального сервера) |
| `MYSQL_PORT` | Порт на хосте (по умолчанию `3306`) |
| `MYSQL_ROOT_PASSWORD` | Пароль пользователя `root` **в контейнере** MySQL; используется только при запуске через Docker Compose (см. `compose.yaml`), в коде приложения не читается |

Пример содержимого — в `.env.example`.

### 3. MySQL

#### Вариант A: Docker Compose

Убедитесь, что Docker установлен и демон запущен. Из корня проекта:

```bash
docker compose up -d
```

(На старых установках может быть команда `docker-compose up -d`.)

Подождите **10–30 секунд**, пока MySQL в контейнере полностью поднимется. Если сразу запустить миграцию, возможна ошибка:

```text
pymysql.err.OperationalError: (2013, 'Lost connection to MySQL server during query')
```

#### Вариант B: свой сервер MySQL

Создайте пользователя и базу с параметрами из `.env`. Пользователю нужны права на работу с базой (для миграции также создаётся БД, если её ещё нет). Пример для пользователя из `.env`:

```sql
GRANT ALL PRIVILEGES ON *.* TO 'kaspersky_user'@'%';
FLUSH PRIVILEGES;
```

### 4. Миграция

Загружает JSON из каталога `data/` в MySQL. Если базы `MYSQL_DATABASE` нет — она будет создана; таблицы пересоздаются при каждом запуске миграции.

```bash
uv run migrate
```

### 5. Приложение

После успешной миграции:

```bash
uv run main
```

Откроется интерактивное меню в терминале.

---

## Стек

| Область | Инструмент |
|---------|------------|
| Контейнеризация | Docker Compose (`compose.yaml`, образ MySQL 8.0) |
| Линтер | [Ruff] |
| Потоковый разбор JSON | [ijson] |
| ORM | [SQLAlchemy] |
| Драйвер MySQL | PyMySQL |
| Конфигурация | python-dotenv |

Проверка линтером:

```bash
uv run ruff check src
```

---

## Декомпозиция проекта

### 1. Схема базы данных

Три связанные таблицы:

**`products`**

- `id` — первичный ключ
- `product_name`, `vendor` — строки
- уникальность пары `(vendor, product_name)`

**`versions`**

- `id` — первичный ключ
- `product_id` — внешний ключ на `products.id`, `ON DELETE CASCADE`
- `version` — строка версии
- уникальность пары `(product_id, version)`

**`vulnerabilities`**

- `id` — первичный ключ
- `product_id` — внешний ключ на `products.id`, `ON DELETE CASCADE`
- `KLA_id`, `description`, `publish_date`, `start_vuln_version`, `fixed_version`

Связи ORM: у продукта — коллекции `versions` и `vulnerabilities`; у версии и уязвимости — ссылка на `product`.

### 2. Слои кода

| Слой | Назначение |
|------|------------|
| **`console`** | CLI: основное меню (`Console`) и сценарий миграции с логами (`MigrationConsole`) |
| **`database`** | Singleton `Database` (движок SQLAlchemy, создание/сброс таблиц, `CREATE DATABASE`), модели в `database/tables/` |
| **`migrations`** | Абстрактный класс `Migration` (батчи из JSON) и реализации: продукты, версии, уязвимости |
| **`utils`** | Парсинг JSON (`ijson`), сравнение версий, запросы к БД для меню, форматирование вывода, `MigrationController`, URL MySQL |
| **`configs`** | Пути к дампам, размер батча, загрузка `.env` |

Точки входа: `main.py` → консоль приложения; `migrate.py` → миграции.

### 3. Сравнение версий

Строки вида `1.2.3` разбиваются по `.`, каждая часть приводится к `int`, получается кортеж `(1, 2, 3)`. Сравнение — лексикографическое сравнение кортежей (как в Python для `tuple`).
