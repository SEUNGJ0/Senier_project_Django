from django.urls import re_path
from . import consumers

''' /ws/chat/ URL로 WebSocket 요청을 처리하고, 이에 해당하는 Consumer 클래스인 SensorConsumer를 실행하도록 설정'''
websocket_urlpatterns = [
    re_path(r'ws/sensor/$', consumers.SensorConsumer.as_asgi()),
]# as__asgi()는 장고의 as_view()와 같은 역할을 한다
