from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter
from .consumer import WeatherConsumer

ws_urlpatterns=[

    path(
        "ws/weather", WeatherConsumer, name="weather"
    ),

]



