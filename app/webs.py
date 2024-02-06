import json
import websockets
import redis
from log import logger
from db import SessionLocal, CurrencyTable

r = redis.Redis(host='localhost', port=6379, db=0)


async def fetch_prices():
    uri = "wss://stream.binance.com:9443/stream?streams=btcusdt@kline_1s/ethusdt@kline_1s"
    async with websockets.connect(uri) as websocket:
        async for message in websocket:
            try:
                exchanger = 'binance'
                data = json.loads(message)
                logger.info(data)
                stream = data['stream']
                if 'btcusdt@kline_1s' in stream:
                    # Обработка данных для BTC к USD
                    kline_data = data['data']['k']
                    close_price = kline_data['c']
                    pair = 'BTC-USD'
                    r.set(pair, close_price)
                    db = SessionLocal()
                    db_text = CurrencyTable(exchanger=exchanger, pair=pair, price=close_price)
                    db.add(db_text)
                    db.commit()
                    db.refresh(db_text)
                    db.close()
                    logger.info(f"Текущая цена {pair}: {close_price}")
                elif 'ethusdt@kline_1s' in stream:
                    # Обработка данных для ETH к USD
                    kline_data = data['data']['k']
                    close_price = kline_data['c']
                    pair = 'BTC-USD'
                    r.set(pair, close_price)
                    db = SessionLocal()
                    db_text = CurrencyTable(exchanger=exchanger, pair=pair, price=close_price)
                    db.add(db_text)
                    db.commit()
                    db.refresh(db_text)
                    db.close()
                    logger.info(f"Текущая цена {pair}: {close_price}")
            except Exception as e:
                logger.error(f"Произошла ошибка при получении данных: {e}")
