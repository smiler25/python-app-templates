from aiohttp import web


async def index(request):
    # await asyncio.sleep(r)
    data = {'result': {'test': 100}}
    return web.json_response(data)


async def stats(request):
    print(request)
    data = {'result': {'test': request.match_info['key']}}
    return web.json_response(data)
