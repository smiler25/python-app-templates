from environs import Env
from sanic import Sanic
from sanic.request import Request

from src.middleware import setup_middlewares
from src.routes import setup_routes
from src.settings import Settings


class AppRequest(Request):
    def get_all_data(self):
        result = self.args
        if self.json:
            result.update(self.json)
        return result


def init_app():
    app = Sanic(__name__, strict_slashes=False)
    env = Env()
    env.read_env()
    app.config.update_config(Settings())
    setup_routes(app)
    setup_middlewares(app)
    app.request_class = AppRequest

    app.run(
        host=app.config.HOST,
        port=app.config.PORT,
        debug=app.config.DEBUG,
        auto_reload=app.config.DEBUG,
    )
    return app


init_app()
