from django.urls import path
from django_webtelnet.tools.channel import websocket


websocket_urlpatterns = [
    path('webtelnet/', websocket.WebTelnet),
]