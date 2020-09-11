"""
ASGI config for Django_socket project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

from Django_socket.websocket import websocket_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Django_socket.settings')

"""
django_application是ASGIHandler()对象，由于这个ASGIHandler()里面实现了__call__方法，所以这个对象还可以进行调用

async def __call__(self, scope, receive, send):

所以下面的async def application(scope, receive, send) 模仿了django_application这个方法（可调用的对象如方法）

class A():
    def __call__(self):
        print('被调用')
a = A()
a()   输出 -->  被调用
看上去可以调用2次的感觉
"""


django_application = get_asgi_application()

async def application(scope, receive, send):
    if scope['type'] == 'http':
        await django_application(scope, receive, send)

    elif scope['type'] == 'websocket':
        await websocket_application(scope, receive, send)
    else:
        raise NotImplementedError(f"Unknown scope type {scope['type']}")

