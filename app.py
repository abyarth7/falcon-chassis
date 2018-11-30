import falcon
import utils
from wsgiref import simple_server

import logging
import uuid
import requests
from images import Resource
import storage

api = application = falcon.API(middleware=[
    utils.AuthMiddleware(),
    utils.RequireJSON(),
    utils.JSONTranslator(),
])
api.add_route('/images', Resource())

db = storage.StorageEngine()
things = utils.ThingsResource(db)
api.add_route('/{user_id}/things', things)

# If a responder ever raised an instance of storage.StorageError, pass control to
# the given handler.
api.add_error_handler(storage.StorageError, storage.StorageError.handle)

# Proxy some things to another service; this example shows how you might
# send parts of an API off to a legacy system that hasn't been upgraded
# yet, or perhaps is a single cluster that all data centers have to share.
sink = utils.SinkAdapter()
api.add_sink(sink, r'/search/(?P<engine>ddg|y)\Z')
# Useful for debugging problems in your API; works with pdb.set_trace(). You
# can also use Gunicorn to host your api. Gunicorn can be configured to
# auto-restart workers when it detects a code change, and it also works
# with pdb.
if __name__ == '__main__':
    httpd = simple_server.make_server('127.0.0.1', 8000, api)
    httpd.serve_forever()