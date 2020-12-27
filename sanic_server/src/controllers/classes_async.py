from sanic.views import HTTPMethodView
from sanic.response import json


class ExampleAsyncView(HTTPMethodView):

    async def get(self, request):
        return json({
            'data': 'async GET result',
            'json': request.json,
            'params': request.args,
            'ip': request.ip,
            'remote_addr': request.remote_addr,
            'request': request.get_all_data(),
        })

    async def post(self, request):
        return json({'data': 'async POST result'})

    async def put(self, request):
        return json({'data': 'async PUT result'})
