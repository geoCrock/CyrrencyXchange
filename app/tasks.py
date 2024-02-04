from celery import Celery
from app.get_rub import usd_to_rub
from app.currency import get_all_cyrrency

celery = Celery('tasks', broker='redis://localhost:6379/0')

broker_connection_retry_on_startup = True


# Каждые 5с получаем актуальные курсы
@celery.task
def get_currency():
    get_all_cyrrency()


# Каждые 60с получаем курс рубля к доллару
@celery.task
def get_rub():
    usd_to_rub()


# Настройка
celery.conf.beat_schedule = {
    'run-every-5-seconds': {
        'task': 'app.tasks.get_currency',
        'schedule': 5.0,  # каждые 5 секунд
    },
    'run-every-60-seconds': {
        'task': 'app.tasks.get_rub',
        'schedule': 60.0,  # каждые 60 секунд
    },
}
