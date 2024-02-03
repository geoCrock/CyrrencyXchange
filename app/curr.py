import aiohttp
import asyncio
from decimal import Decimal


async def fetch_exchange_rate():
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            return Decimal(str(data['rates']['RUB']))


async def main():
    exchange_rate = await fetch_exchange_rate()
    print(f"Текущий курс доллара к рублю: 1 USD = {exchange_rate} RUB")

if __name__ == "__main__":
    asyncio.run(main())