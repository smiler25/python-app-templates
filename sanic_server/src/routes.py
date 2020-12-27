from .controllers import classes_async, classes_sync, simple, websocket


def setup_routes(app):
    app.add_route(simple.example, '/simple')
    app.add_route(classes_async.ExampleAsyncView.as_view(), '/async')
    app.add_route(classes_sync.ExampleView.as_view(), '/sync')
    app.add_websocket_route(websocket.feed, '/feed')
