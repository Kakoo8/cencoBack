# Built in imports.
import json
import datetime
import threading
# Third Party imports.
from channels.exceptions import DenyConnection
from channels.generic.websocket import AsyncWebsocketConsumer
# Django imports.
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import AnonymousUser
from .views import get_weather
class WeatherConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        print("Connected")
        await self.send_json()
        print("Sended")
  

    async def disconnect(self, close_code):
        print("Disconnected")
        pass

    async def send_json(self):
        """
        Encode the given content as JSON and send it to the client.
        """
        await self.send(text_data=json.dumps(get_weather("params")))
        
        
