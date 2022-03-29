
from django.urls import re_path

from game.consumers import TicTacToeConsumer

websocket_urlpatterns = [
    re_path(r'^ws/play/(?P<room_code>\w+)/$', TicTacToeConsumer.as_asgi()),
]