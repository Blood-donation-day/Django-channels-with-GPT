import os

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

django_asgi_app = get_asgi_application()

# app.routing 임포트는 여기에 !!!
# 🔥 HERE
import chat.routing  # noqa


application = ProtocolTypeRouter(
    {
        "http": django_asgi_app,
        #채널스 기본에서는 쿠키/세션/인증을 비활성화 // self.scope에서 접근가능
        #self.scope["user"].is_authenticated 에서 인증여부 확인
        "websocket": AuthMiddlewareStack(
            URLRouter(chat.routing.websocket_urlpatterns),
        ),
    }
)