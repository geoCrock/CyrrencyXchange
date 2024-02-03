from celery import Celery
import aiohttp
import asyncio
import aioredis

# Создание объекта Celery с поддержкой асинхронности
celery_app = Celery('async_tasks', backend='redis://localhost', broker='redis://localhost')

# Функция для получения данных из API и сохранения их в Redis
async def get_data_and_store():
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get('https://api.example.com/data') as response:
                data = await response.json()
                redis = await aioredis.create_redis_pool('redis://localhost')
                await redis.set('ключ', str(data))
                redis.close()
                await redis.wait_closed()
                print("Данные успешно получены и сохранены в Redis.")
    except Exception as e:
        print("Ошибка при получении данных:", e)


# Определение асинхронной задачи Celery
@celery_app.task
async def async_get_data_and_store():
    await get_data_and_store()
