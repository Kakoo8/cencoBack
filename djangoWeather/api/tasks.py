import requests
import redis
import json
import datetime
import random
from asgiref.sync import async_to_sync
from django.conf import settings
from channels.layers import get_channel_layer
from asgiref.sync import AsyncToSync
from rest_framework import status
from rest_framework.response import Response
from channels.layers import get_channel_layer
from .models import Weather
from celery import shared_task
redis = redis.StrictRedis(host=settings.REDIS_HOST,port=settings.REDIS_PORT, db=0)


channel_layer = get_channel_layer()
@shared_task
def get_weather():

    cities = ['London', 'Santiago', 'Zurich', 'Auckland', 'Sydney', 'Georgia']
    data = []
    params=""
    for city in cities:

        lat = json.loads(redis.get(city + 'Lat'))

        lon = json.loads(redis.get(city + 'Lon'))

        url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=c373cc5c75cb95bd584db9668289be86"
        data.append(get_dataW(url, city, params))
    AsyncToSync(channel_layer.send)("channel_name",{"type": "celery.message","text": json.dumps(data)})
    



def get_dataW(url, city, args):
        time = datetime.datetime.now()
        if (random.uniform(0, 1) < 0.1):

            redis.set(time.timestamp(), "error Consulting "+city)
            get_dataW(url, city, args)

        else:
            redis.set(time.timestamp(), "error Consulting "+city)
            response = generate_request(url, args)
            if response:
                return response


def generate_request(url, params={}):
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()
