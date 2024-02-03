import aiohttp
from decimal import Decimal

import redis

r = redis.Redis(host='localhost', port=6379, db=0)


async def usd_to_rub():
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            r.set('rub', str(data['rates']['RUB']))
            return Decimal(str(data['rates']['RUB']))


# async def usd_to_rub():
#     exchange_rate = await fetch_exchange_rate()
#     print(f"Текущий курс доллара к рублю: 1 USD = {exchange_rate} RUB")
#     await r.set('rub', exchange_rate)
