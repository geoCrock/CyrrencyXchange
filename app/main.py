import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager

from currency import get_all_cyrrency
from currency import r
from get_rub import usd_to_rub


@asynccontextmanager
async def lifespan(app: FastAPI):
    await usd_to_rub()
    await get_all_cyrrency()
    yield

app = FastAPI(lifespan=lifespan)


@app.get("/v1/courses/{currency}")
async def get_exchange_rate(currency: str):
    currency = currency.replace('-', '/')
    try:
        return r.get(currency).decode('utf-8')
    except Exception:
        return 'Нет данных на эту пару валют'


@app.get('/test')
async def test():
    return 'hi!'


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
