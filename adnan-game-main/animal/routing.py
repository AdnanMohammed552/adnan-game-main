from django.urls import path

from . import consumers
websocket_urlpatterns= [
    path('ws/<int:room_code>/' , consumers.gameConsumer.as_asgi()),
]
