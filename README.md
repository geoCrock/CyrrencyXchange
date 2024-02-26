# CirrencyXchange

## Description

## Peculiarities

Available cryptocurrencies: USDT, BCT, ETH
Currency rates available: RUB, UDF

Currency pairs look like this: “BTC-USD”, “ETH-RUB”, “USDT-RUB”, etc.

## Run via docker-compose

1. Create `.env` and put the postgres url

      ```env
      POSTGRES_URL = "postgresql://postgresql:postgresql@localhost/cyrrency"
      ```

2. Launch

     ```bash
     docker compose up --build
     ```

## Launch

1. Create `venv`

2. Create `.env` and put the postgres url

      ```env
      POSTGRES_URL = "postgresql://postgresql:postgresql@localhost/cyrrency"
      ```
3. Install dependencies

    ```bash
    RUN pip install --upgrade pip
    RUN pip install -r requirements.txt
    ```
4. Launch

    ```bash
    uvicorn app.main:app --host 127.0.0.1 --port 8000
    ```
