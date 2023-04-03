from django.urls import path

from . import consumers

websocket_urlpatterns= [
    path('ws/<int:room_code>/quiz/' , consumers.gameConsumer.as_asgi()),
]