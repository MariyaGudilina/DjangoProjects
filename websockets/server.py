import os

from aiohttp import web, ClientSession

WS_FILE = os.path.join(os.path.dirname(__file__), 'websocket.html')


async def wshandler(request: web.Request):
    resp = web.WebSocketResponse()
    available = resp.can_prepare(request)
    if not available:
        with open(WS_FILE, "rb") as fp:
            return web.Response(body=fp.read(), content_type="text/html")

    await resp.prepare(request)

    await resp.send_str("Привет!!!")

    try:
        print("Someone joined.")
        for ws in request.app["sockets"]:
            await ws.send_str("Someone joined")
        request.app["sockets"].append(resp)

        async for msg in resp:
            if msg.type == web.WSMsgType.TEXT:
                for ws in request.app["sockets"]:
                    if ws is not resp:
                        await ws.send_str(msg.data)
            else:
                return resp
        return resp

    finally:
        request.app["sockets"].remove(resp)
        print("Someone disconnected.")
        for ws in request.app["sockets"]:
            await ws.send_str("Someone disconnected.")


async def on_shutdown(app: web.Application):
    for ws in app["sockets"]:
        await ws.close()


async def post_handler(request):
    data_request = await request.json()
    #text_news='news news'
    text_news = data_request.text
    async with ClientSession().ws_connect('http://localhost:8080/') as ws:
        await ws.post.send_str(text_news)
        await ws.close()
    data = {"status": "ok"}
    return web.json_response(data)


def init():
    app = web.Application()
    app["sockets"] = []
    app.router.add_get("/", wshandler)
    app.router.add_post("/post", post_handler)
    app.on_shutdown.append(on_shutdown)
    return app


web.run_app(init())

