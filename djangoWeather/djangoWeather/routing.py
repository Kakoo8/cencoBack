from channels.routing import ProtocolTypeRouter, URLRouter
from api.routing import websockets


application = ProtocolTypeRouter({
    "websocket": websockets,
})
