from django.urls import path

from . import consumers

websocket_urlpatterns= [
    path('xws/<int:room_code>/admin/' , consumers.gameConsumer.as_asgi()),
]