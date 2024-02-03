import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager

from cctx2 import main
from cctx2 import r


@asynccontextmanager
async def lifespan(app: FastAPI):
    await main()
    yield

app = FastAPI(lifespan=lifespan)


@app.get("/v1/courses/{currency}")
async def get_exchange_rate(currency: str):
    return r.get(currency).decode('utf-8')
    # value = await update_exchange_rates(symbol)
    # return {"exchanger": "binance", "courses": [{"direction": symbol, "value": value}]}


@app.get('/test')
async def test():
    return "hi!"


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
