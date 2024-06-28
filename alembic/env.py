import sys
import os
from logging.config import fileConfig
from sqlalchemy import create_engine, pool
from alembic import context
from dotenv import load_dotenv

# Загрузка переменных окружения из файла .env
load_dotenv()

# Конфигурация логирования из файла ini
fileConfig(context.config.config_file_name)

# Настройка SQLAlchemy engine и MetaData
config = context.config

# Получение строки подключения из переменных окружения
db_user = os.getenv("DB_USER", "fizi")
db_password = os.getenv("DB_PASSWORD", "1234")
db_name = os.getenv("DB_NAME", "fizi_db")
db_host = os.getenv("DB_HOST", "localhost")
db_port = os.getenv("DB_PORT", "5432")

DATABASE_URL = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models import Base  # импорт моделей

target_metadata = Base.metadata

def run_migrations_offline():
    """Запуск миграций в 'offline' режиме."""
    url = DATABASE_URL
    context.configure(
        url=url, target_metadata=target_metadata, literal_binds=True
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """Запуск миграций в 'online' режиме."""
    connectable = create_engine(DATABASE_URL, poolclass=pool.NullPool)

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
