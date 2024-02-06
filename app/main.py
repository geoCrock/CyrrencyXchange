import asyncio
import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager
from log import logger
from webs import r
from webs import fetch_prices
from db import SessionLocal, CurrencyTable
# from currency import get_all_cyrrency
# from get_rub import usd_to_rub


@asynccontextmanager
async def lifespan(app: FastAPI):
    asyncio.create_task(forever_job_function())
    yield


app = FastAPI(lifespan=lifespan)


async def forever_job_function():
    while True:
        await fetch_prices()


@app.get("/v1/courses/{currency}")
async def get_exchange_rate(pair: str):
    pair = pair.upper()
    try:
        # list_values = r.lrange(currency, 0, -1)
        return {'exchanger': 'binance',
                "courses":
                    [{'direction': pair, 'value': r.get(pair).decode('utf-8')}]}
    except 'NoneType' as e:
        logger.warning(f'Не правильная пара "{pair}" : {e}')
        return 'Нет данных на эту пару валют'
    except Exception as e:
        logger.error(f'Произошла ошибка: {e}')
        return 'Нет данных на эту пару валют'


# @app.get("/v1/courses/all_courses")
# async def all_courses():
#     try:
#         # list_values = r.lrange(currency, 0, -1)
#         return {'exchanger': 'binance',
#                 "courses":
#                     [{'direction': pair, 'value': r.get(pair).decode('utf-8')}]}
#     except 'NoneType' as e:
#         logger.warning(f'Не правильная пара "{pair}" : {e}')
#         return 'Нет данных на эту пару валют'
#     except Exception as e:
#         logger.error(f'Произошла ошибка: {e}')
#         return 'Нет данных на эту пару валют'


@app.get("/v1/courses/all_courses_history")
async def get_all_courses():
    try:
        db = SessionLocal()
        db_text = (db.query(CurrencyTable.exchanger, CurrencyTable.datetime, CurrencyTable.pair, CurrencyTable.price)
                   .order_by(CurrencyTable.id.desc()).all())
        db.close()
        print(db_text)
        return str(db_text)
    except Exception as e:
        logger.error(e)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
