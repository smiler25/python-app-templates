import logging
from flask import Flask, jsonify
from flask_restful import Api

from .controllers import ExampleAPI
from .utils import MongoJSONEncoder
from .settings import SERVICE_NAME


def init_app():
    app = Flask(__name__)
    api = Api(app)
    app.json_encoder = MongoJSONEncoder
    app.url_map.strict_slashes = False
    app.config.update(JSONIFY_PRETTYPRINT_REGULAR=False)

    api.add_resource(ExampleAPI, '/example')

    # @app.teardown_appcontext
    # def close_db(*args, **kwargs):
    #     from flask import g
    #     if hasattr(g, 'mongodb'):
    #         g.mongodb.close()

    @app.errorhandler(Exception)
    def handle_all_errors(error):
        logging.getLogger(SERVICE_NAME).error('handle_all_errors: {}'.format(error), exc_info=True)
        response = jsonify({'error': 'An error occurred on the server'})
        return response, 500

    return app


app = init_app()


if __name__ == '__main__':
    app.run(debug=True)
