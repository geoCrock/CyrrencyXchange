import asyncio
import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.log import logger
from app.webs import r
from app.webs import fetch_prices
from app.get_rub import usd_to_rub
from app.get_rub import set_usdt_usd


@asynccontextmanager
async def lifespan(app: FastAPI):
    await set_usdt_usd()
    await usd_to_rub()
    asyncio.create_task(forever_job_function())
    yield


app = FastAPI(lifespan=lifespan)


async def forever_job_function():
    await fetch_prices()


@app.get("/v1/courses/{currency}")
async def get_exchange_rate(pair: str):
    pair = pair.upper()
    try:
        return {'exchanger': 'binance',
                "courses":
                    [{'direction': pair, 'value': r.get(pair).decode('utf-8')}]}
    except 'NoneType' as e:
        logger.warning(f'Не правильная пара "{pair}" : {e}')
        return 'Нет данных на эту пару валют'
    except Exception as e:
        logger.error(f'Произошла ошибка: {e}')
        return 'Нет данных на эту пару валют'


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
