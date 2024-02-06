import aiohttp
from app.currency import r
from log import logger


async def set_usdt_usd():
    r.set('USDT-USD', '1')


async def usd_to_rub():
    try:
        url = 'https://api.exchangerate-api.com/v4/latest/USD'
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                data = await response.json()
                rub = str(data['rates']['RUB'])
                r.set('rub', rub)
                r.set('USDT-RUB', rub)
                logger.info(f"Получили курс рубля к доллару {rub}")
    except Exception as e:
        logger.error(f'Произошла ошибка получения курса доллара к рублю: {e}')
