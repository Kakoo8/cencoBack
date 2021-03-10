# Built in imports.
import json
# Third Party imports.
from channels.exceptions import DenyConnection
from channels.generic.websocket import AsyncWebsocketConsumer
# Django imports.
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import AnonymousUser
from .views import get_weather
class weatherConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        print("Conected")
        await self.send(text_data=json.dumps(get_weather("params")))
        print("Sended")

    async def disconnect(self, close_code):
        pass


    async def celery_message(self, event):
        print("Service Received")
        print(event)
        await self.send({
            "type": "websocket.send",
            "text": event["text"],
        })
