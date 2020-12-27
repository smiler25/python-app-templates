from sanic.response import json


async def example(request):
    return json({"test": True})
