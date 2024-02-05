import aiohttp
from app.currency import r
from log import logger


async def usd_to_rub():
    try:
        url = 'https://api.exchangerate-api.com/v4/latest/USD'
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                data = await response.json()
                r.set('rub', str(data['rates']['RUB']))
                logger.info(f"Получили курс рубля к доллару {str(data['rates']['RUB'])}")
    except Exception as e:
        logger.warning(f'Произошла ошибка получения курса доллара к рублю: {e}')
