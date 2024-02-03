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
            r.set(pair, ask_price)
            value = r.get(pair).decode('utf-8')
            print(f'Установилось значение для редис на {pair}: {value}')
            return ask_price
    except ccxt.NetworkError as e:
        print(f"Ошибка сети при обращении к {exchange.id}: {e}")
    except ccxt.ExchangeError as e:
        print(f"Ошибка биржи {exchange.id}: {e}")
    except Exception as e:
        print(f"Необработанная ошибка при обращении к {exchange.id}: {e}")
    return None


async def get_all_cyrrency():
    # Создаем список бирж, к которым хотим подключиться
    exchanges = (ccxt.kraken(), ccxt.bitfinex())

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
    for pair, rate in zip(currency_pairs, results):
        if rate is not None:
            currency_rates[pair] = rate

    # Закрываем ресурсы для каждой биржи
    for exchange in exchanges:
        await exchange.close()

    return currency_rates

# Запускаем асинхронный код
# currency_rates = asyncio.run(get_all_cyrrency())

# Выводим найденные курсы
# print("Найденные курсы:")
# for pair, rate in currency_rates.items():
#     print(f"{pair}: {rate}")