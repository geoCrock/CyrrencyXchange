from celery.schedules import crontab

CELERY_IMPORTS = ('async_tasks',)

CELERYBEAT_SCHEDULE = {
    'get-data-every-5-seconds': {
        'task': 'async_tasks.async_get_data_and_store',
        'schedule': 5.0,
    },
}
