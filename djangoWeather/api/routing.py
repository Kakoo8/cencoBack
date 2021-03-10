from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter
from .consumer import weatherConsumer
websockets = URLRouter([
    path(
        "ws/weather", weatherConsumer,
        name="weather",
    ),
])
