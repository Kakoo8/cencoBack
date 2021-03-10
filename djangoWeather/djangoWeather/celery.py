import os
from celery import Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE','djangoWeather.settings')

app= Celery('djangoWeather')
app.config_from_object('django.conf:settings',namespace='CELERY')


app.conf.beat_schedule = {

    'get_weathers_10s':{
        'task': 'api.tasks.get_weather',
        'schedule': 10.0
    }
}
app.autodiscover_tasks()