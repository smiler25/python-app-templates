from sanic.views import HTTPMethodView
from sanic.response import text, json


class ExampleView(HTTPMethodView):

    def get(self, request):
        return json({'data': 'sync GET result'})

    def post(self, request):
        return json({'data': 'sync POST result'})

    def put(self, request):
        return json({'data': 'sync PUT result'})

    def patch(self, request):
        return json({'data': 'sync PATCH result'})

    def delete(self, request):
        return json({'data': 'sync DELETE result'})
