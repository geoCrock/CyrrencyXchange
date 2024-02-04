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
    currency = currency.replace('-', '/').upper()
    try:
        list_values = r.lrange(currency, 0, -1)
        return {'exchanger': list_values[0].decode('utf8'),
                "courses":
                    [{'direction': currency, 'value': list_values[1].decode('utf-8')}]}
    except Exception:
        return 'Нет данных на эту пару валют'


@app.get('/test')
async def test():
    return 'hi!'


@app.get('/test2')
async def test():
    return r.get('rub').decode('utf-8')


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
