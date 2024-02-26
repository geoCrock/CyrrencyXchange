# CyrrencyXchange

Пары валют выглядат так: BTC-USD, ETH-RUB, USDT-RUB и т.д.

## Запуск через docker-compose

1. Создать `.env` и положить url postgres

     ```env
     POSTGRES_URL = "postgresql://postgresql:postgresql@localhost/cyrrency"
     ```

2. Запустить

    ```bash
    docker compose up --build
    ```

## Запуск

1. Создать `venv`

2. Создать `.env` и положить url postgres

     ```env
     POSTGRES_URL = "postgresql://postgresql:postgresql@localhost/cyrrency"
     ```
3. Установить зависимости

   ```bash
   RUN pip install --upgrade pip
   RUN pip install -r requirements.txt
   ```
4. Запустить

   ```bash
   uvicorn app.main:app --host 127.0.0.1 --port 8000
   ```
