# from decimal import Decimal
# import ccxt.async_support as ccxt
# import redis
# from log import logger
#
# r = redis.Redis(host='localhost', port=6379, db=0)
#
#
# async def add_to_redis_rub(pair, exchange_id, ask_price):
#     pair = pair.replace('/USD', '/RUB')
#     rub = Decimal(r.get('rub').decode('utf-8'))
#     ask_price = Decimal(ask_price)
#     ask_price = round(ask_price * rub, 2)
#     ask_price = str(ask_price)
#     info_list = [exchange_id, ask_price]
#     r.delete(pair)
#     r.rpush(pair, *info_list)
#     logger.info(f'Установилось значение в redis на {pair}: {r.lrange(pair, 0, -1)}')
#
#
# async def add_to_redis_usd(pair, exchange_id, ask_price):
#     info_list = [exchange_id, ask_price]
#     r.delete(pair)
#     r.rpush(pair, *info_list)
#     logger.info(f'Установилось значение в redis на {pair}: {r.lrange(pair, 0, -1)}')
#
#
# async def fetch_ticker(exchange, pair):
#     try:
#         ticker = await exchange.fetch_ticker(pair)
#         ask_price = ticker['ask']
#         # logger.info(f"Курс для {pair} на {exchange.id}: Ask - {ask_price}")
#         if not ask_price == 'None':
#             await add_to_redis_usd(pair, exchange.id, ask_price)
#             await add_to_redis_rub(pair, exchange.id, ask_price)
#         return ask_price  # Возвращаем полученное значение
#     except ccxt.NetworkError as e:
#         logger.warning(f"Ошибка сети при обращении к {exchange.id}: {e}")
#     except ccxt.ExchangeError as e:
#         logger.warning(f"Ошибка биржи {exchange.id}: {e}")
#     except Exception as e:
#         logger.warning(f"Необработанная ошибка при обращении к {exchange.id}: {e}")
#     return None
#
#
# async def get_all_cyrrency():
#     # Создаем список бирж, к которым хотим подключиться
#     exchanges = (ccxt.kraken(), ccxt.bitfinex(), ccxt.binance(), ccxt.coinex(),
#                  ccxt.coinbase(), ccxt.huobi(), ccxt.bitstamp(), ccxt.gateio())
#
#     # Определяем валютные пары, для которых хотим получить курсы
#     currency_pairs = ('BTC/USD', 'ETH/USD', 'USDT/USD')
#
#     # Создаем словарь для хранения уже полученных значений курсов
#     cached_tickers = {}
#
#     # Создаем список задач для выполнения асинхронно
#     for pair in currency_pairs:
#         for exchange in exchanges:
#             # Проверяем, есть ли уже значение в кэше
#             if pair not in cached_tickers:
#                 # Если нет, делаем запрос и сохраняем значение в кэше
#                 cached_tickers[pair] = await fetch_ticker(exchange, pair)
#             else:
#                 # Если значение уже есть в кэше, используем его
#                 # logger.info(f"Значение для {pair} уже получено: {cached_tickers[pair]}")
#                 pass
#
#     # Закрываем ресурсы для каждой биржи
#     for exchange in exchanges:
#         await exchange.close()
#
#     logger.info(f'Кэш: {cached_tickers}')
#
