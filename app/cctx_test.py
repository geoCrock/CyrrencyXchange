import ccxt.async_support as ccxt
import asyncio


async def fetch_ticker(exchange, pair):
    try:
        ticker = await exchange.fetch_ticker(pair)
        ask_price = ticker['ask']
        print(f"Курс для {pair} на {exchange.id}: Ask - {ask_price}")
    except ccxt.NetworkError as e:
        print(f"Ошибка сети при обращении к {exchange.id}: {e}")
    except ccxt.ExchangeError as e:
        print(f"Ошибка биржи {exchange.id}: {e}")
    except Exception as e:
        print(f"Необработанная ошибка при обращении к {exchange.id}: {e}")


async def main():
    # Создаем список бирж, к которым хотим подключиться
    exchanges = [ccxt.kraken(), ccxt.bitfinex()]

    # Определяем валютные пары, для которых хотим получить курсы
    currency_pairs = ['BTC/USD', 'ETH/USD', 'USDT/USD']

    # Создаем список задач для выполнения асинхронно
    tasks = []
    for pair in currency_pairs:
        for exchange in exchanges:
            tasks.append(fetch_ticker(exchange, pair))

    # Запускаем все задачи и ждем их завершения
    await asyncio.gather(*tasks)

    # Закрываем ресурсы для каждой биржи
    for exchange in exchanges:
        await exchange.close()


# Запускаем асинхронный код
asyncio.run(main())
