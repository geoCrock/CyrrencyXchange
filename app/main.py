import asyncio
import uvicorn
from fastapi import FastAPI
from currency import r
from currency import get_all_cyrrency
from get_rub import usd_to_rub
from log import logger
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    asyncio.create_task(async_job_function())
    yield


app = FastAPI(lifespan=lifespan)


async def async_job_function():
    while True:
        await usd_to_rub()
        await get_all_cyrrency()


@app.get("/v1/courses/{currency}")
async def get_exchange_rate(currency: str):
    currency = currency.replace('-', '/').upper()
    try:
        list_values = r.lrange(currency, 0, -1)
        return {'exchanger': list_values[0].decode('utf8'),
                "courses":
                    [{'direction': currency, 'value': list_values[1].decode('utf-8')}]}
    except Exception as e:
        logger.warning(f'Произошла ошибка: {e}')
        return 'Нет данных на эту пару валют'


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
