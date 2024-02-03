import aiohttp

import uvicorn
from fastapi import FastAPI

app = FastAPI()


async def update_exchange_rates(symbol):
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(f'https://api.binance.com/api/v3/ticker/price?symbol={symbol}') as response:
                data = await response.json()
                if 'price' in data:
                    return float(data['price'])
                else:
                    return f"Error: No 'price' key in response for symbol: {symbol} or symbol in not exist"
        except Exception as e:
            return f"Error: fetching data for symbol {symbol}: {e}"


@app.get("/courses/{symbol}")
async def get_exchange_rate(symbol: str):
    value = await update_exchange_rates(symbol)
    return {"exchanger": "binance", "courses": [{"direction": symbol, "value": value}]}


@app.get('/test')
async def test():
    return 'hi!'


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)