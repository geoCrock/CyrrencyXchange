import asyncio
import websockets
import json


async def fetch_prices():
    uri = "wss://stream.binance.com:9443/stream?streams=btcusdt@kline_5s/ethusdt@kline_5s/usdtusdt@kline_5s"
    async with websockets.connect(uri) as websocket:
        async for message in websocket:
            try:
                data = json.loads(message)
                print(data)
                stream = data['stream']
                if 'btcusdt@kline_5s' in stream:
                    # Обработка данных для BTC к USD
                    kline_data = data['data']['k']
                    close_price = kline_data['c']
                    print(f"Текущая цена BTC к USD (5-минутный интервал): {close_price}")
                elif 'ethusdt@kline_5s' in stream:
                    # Обработка данных для ETH к USD
                    kline_data = data['data']['k']
                    close_price = kline_data['c']
                    print(f"Текущая цена ETH к USD (5-минутный интервал): {close_price}")
                elif 'usdtusdt@kline_5s' in stream:
                    # Обработка данных для USDT к USD
                    ticker_data = data['data']
                    price = ticker_data['c']
                    print(f"Текущая цена USDT к USD: {price}")
            except Exception as e:
                print(f"Произошла ошибка при получении данных: {e}")


async def main():
    await fetch_prices()

if __name__ == "__main__":
    asyncio.run(main())
