import aiohttp
from app.currency import r


async def usd_to_rub():
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            r.set('rub', str(data['rates']['RUB']))
            print(f"Получили курс рубля к доллару {str(data['rates']['RUB'])}")
