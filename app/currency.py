import ccxt.async_support as ccxt
import asyncio
import redis

r = redis.Redis(host='localhost', port=6379, db=0)


async def fetch_ticker(exchange, pair):
    try:
        ticker = await exchange.fetch_ticker(pair)
        ask_price = ticker['ask']
        print(f"Курс для {pair} на {exchange.id}: Ask - {ask_price}")
        if not ask_price == 'None':
            info_list = [exchange.id, ask_price]
            r.delete(pair)
            r.rpush(pair, *info_list)
            list_values = r.lrange(pair, 0, -1)
            print(f'Лист который попал в redis: {list_values}')
            print(f'Установилось значение для redis на {pair}: {ask_price}')
            return pair
    except ccxt.NetworkError as e:
        print(f"Ошибка сети при обращении к {exchange.id}: {e}")
    except ccxt.ExchangeError as e:
        print(f"Ошибка биржи {exchange.id}: {e}")
    except Exception as e:
        print(f"Необработанная ошибка при обращении к {exchange.id}: {e}")
    return None


async def get_all_cyrrency():
    # Создаем список бирж, к которым хотим подключиться
    # exchanges = (ccxt.kraken(), ccxt.bitfinex(),)
    exchanges = (ccxt.kraken(),)

    # Определяем валютные пары, для которых хотим получить курсы
    currency_pairs = ('BTC/USD', 'ETH/USD', 'USDT/USD')

    # Создаем словарь для хранения курсов
    currency_rates = {}

    # Создаем список задач для выполнения асинхронно
    tasks = []
    for pair in currency_pairs:
        for exchange in exchanges:
            tasks.append(fetch_ticker(exchange, pair))

    # Запускаем все задачи и ждем их завершения
    results = await asyncio.gather(*tasks)

    # Заполняем словарь найденными курсами
    # for pair, rate in zip(currency_pairs, results):
    #     if rate is not None:
    #         currency_rates[pair] = rate

    # Закрываем ресурсы для каждой биржи
    for exchange in exchanges:
        await exchange.close()

    return currency_rates
