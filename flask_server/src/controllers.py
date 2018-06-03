from flask_restful import Resource, reqparse


class ExampleAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('data', location='json')
        self.reqparse.add_argument('some_key', type=str, location='json')
        super().__init__()

    def get(self, key=None):
        args = self.reqparse.parse_args()
        return True

    def post(self):
        return True

    def delete(self):
        return True
