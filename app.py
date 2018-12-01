import falcon
from wsgiref import simple_server
from controllers.images import Resource

api = application = falcon.API(middleware=[])


# ADD URLS HERE
api.add_route('/images', Resource())

if __name__ == '__main__':
    httpd = simple_server.make_server('127.0.0.1', 8000, api)
    httpd.serve_forever()