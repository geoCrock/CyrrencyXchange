# CirrencyXchange


## Description

CirrencyXchange: Stay Updated with Real-Time Currency Pairs!

Never miss a beat in the dynamic world of forex trading with our WebSocket Forex Watcher. This project provides a seamless solution for tracking and visualizing real-time currency pairs directly through WebSocket connections. Say goodbye to outdated data and hello to instantaneous updates on currency pairs' fluctuations, enabling traders to make informed decisions at the speed of the market.

Key Features:

1. Real-Time Updates: Experience currency pairs' movements as they happen, ensuring you're always in sync with the latest market trends.
2. WebSocket Integration: Leveraging WebSocket technology for efficient and low-latency data transmission, guaranteeing timely updates without overwhelming server loads.
3. Cross-Platform Compatibility: Accessible from any device with internet connectivity, ensuring you're connected to the market wherever you are.

Whether you're a seasoned trader or just getting started, our WebSocket Forex Watcher empowers you with the real-time data you need to thrive in the fast-paced world of currency trading. Dive in, stay informed, and trade with confidence!


## Peculiarities

Available cryptocurrencies: USDT, BCT, ETH
Currency rates available: RUB, USD

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
