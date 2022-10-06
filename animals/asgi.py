from email.mime import application
import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter,URLRouter

from django.core.asgi import get_asgi_application

import animal.routing
import gameadmin.routing
import letter.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'animals.settings')

application = ProtocolTypeRouter({

    'websocket': AuthMiddlewareStack(
        URLRouter(
            animal.routing.websocket_urlpatterns+
            gameadmin.routing.websocket_urlpatterns+
            letter.routing.websocket_urlpatterns
        )
    )
})