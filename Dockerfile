# Используем базовый образ Python
FROM python:3.10

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы зависимостей и устанавливаем их
COPY pyproject.toml poetry.lock ./
RUN pip install poetry && poetry install

# Копируем остальные файлы проекта
COPY . .

# Команда для запуска приложения
CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
