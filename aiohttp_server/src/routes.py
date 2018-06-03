from aiohttp import web

from .controllers import index, stats


def setup_routes(app):
    app.add_routes([
        web.get('/', index),
        web.post('/stats/{key}', stats),
    ])
