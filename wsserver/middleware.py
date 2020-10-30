from django.urls import resolve
from . import connection

def websockets(app):
    async def asgi(scope, receive, send):
        if scope["type"] == "websocket":
            match = resolve(scope["raw_path"])
            await match.func(connection.WebSocket(scope, receive, send), *match.args, **match.kwargs)
            return
        await app(scope, receive, send)
    return asgi