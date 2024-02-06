import json
from decimal import Decimal
import websockets
import redis
from log import logger
from db import SessionLocal, CurrencyTable

r = redis.Redis(host='localhost', port=6379, db=0)


async def add_ro_r_db(exchanger, pair, price):
    r.set(pair, price)
    logger.info(f"Добавленно в redis {pair}: {price}")
    db = SessionLocal()
    db_text = CurrencyTable(exchanger=exchanger, pair=pair, price=price)
    db.add(db_text)
    db.commit()
    db.refresh(db_text)
    db.close()


async def add_to_r_db_rub(exchanger, pair, price):
    pair_ru = pair.replace('-USD', '-RUB')
    rub = Decimal(r.get('rub').decode('utf-8'))
    price = Decimal(price)
    price_ru = str(round(price * rub, 2))
    r.set(pair_ru, price_ru)
    logger.info(f'Добавленно в redis {pair_ru}: {price_ru}')
    db = SessionLocal()
    db_text = CurrencyTable(exchanger=exchanger, pair=pair_ru, price=price_ru)
    db.add(db_text)
    db.commit()
    db.refresh(db_text)
    db.close()
    logger.info(f"Добавленно в db {pair_ru}: {price_ru}")


async def fetch_prices():
    uri = "wss://stream.binance.com:9443/stream?streams=btcusdt@kline_1m/ethusdt@kline_1m"
    async with websockets.connect(uri) as websocket:
        async for message in websocket:
            try:
                exchanger = 'binance'
                data = json.loads(message)
                stream = data['stream']
                if 'btcusdt@kline_1m' in stream:
                    price = data['data']['k']['c']
                    pair = 'BTC-USD'
                    await add_ro_r_db(exchanger, pair, price)
                    await add_to_r_db_rub(exchanger, pair, price)
                elif 'ethusdt@kline_1m' in stream:
                    price = data['data']['k']['c']
                    pair = 'ETH-USD'
                    await add_ro_r_db(exchanger, pair, price)
                    await add_to_r_db_rub(exchanger, pair, price)

                    logger.info(f"Добавленно в db {pair}: {price}")
            except Exception as e:
                logger.error(f"Произошла ошибка при получении данных: {e}")
