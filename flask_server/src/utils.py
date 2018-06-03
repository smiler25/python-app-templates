import json
from datetime import datetime

from flask.json import JSONEncoder


class MongoJSONEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.strftime('%Y-%d-%m %H:%M:%S')
        return json.JSONEncoder.default(self, o)
