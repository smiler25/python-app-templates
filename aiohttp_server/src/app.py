from aiohttp import web

from src import settings
from src.middleware import setup_middlewares
from src.routes import setup_routes


async def init_app():
    app = web.Application()
    setup_routes(app)
    setup_middlewares(app)
    app['config'] = settings

    # app.on_startup.append(init_db)
    # app.on_cleanup.append(close_db)
    return app


if __name__ == '__main__':
    web.run_app(init_app(), host='127.0.0.1')
