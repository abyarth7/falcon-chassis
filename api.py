import falcon
from wsgiref import simple_server
from app.controllers.images import Resource
from app.controllers.Order import Order
from app.controllers.GetOrderDetails import GetOrderDetails
from app.controllers.GetUserHistory import GetUserHistory
# from app.middlewares.db_session_manager import SessionManager
# from config.db_client import Session

# session = Session()

api = falcon.API(middleware=[
    # SessionManager(session),
])


# ADD URLS HERE
api.add_route('/order/details', Order())
api.add_route('/order/getorderitem', GetOrderDetails())
api.add_route('/order/getuserhistory', GetUserHistory())

if __name__ == '__main__':
    httpd = simple_server.make_server('127.0.0.1', 8000, api)
    httpd.serve_forever()
