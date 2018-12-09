import falcon
import json
from app.utils.db_connect import DBConnect
from logger import set_up_logging
from app.models.schema import OrderCart, OrderDetails, PhleboDetails, PickupAddress, PaymentDetails
from config.base import Session, engine, Base

logger = set_up_logging()

# generate database schema
Base.metadata.create_all(engine)
# create a new session
session = Session()


class GetUserHistory(object):
    """Serves all apis related to Orders
    """

    def on_get(self, req, resp):
        try:
            cart_order = session.query(OrderCart).filter_by(patient_id=426).all()
            data = []
            for item in cart_order:
                order = {
                    'phlebo_name': item.phlebo_detail.phlebo_name,
                    'phlebo_number': item.phlebo_detail.phlebo_phone
                }
                data.append(order)

            logger.info("Data fetched successfully : {}".format("Success"))
            resp.body = json.dumps({"message":"Success","data":data})
            resp.status = falcon.HTTP_200
        except Exception as error:
            logger.error("Data fetched failed due to : {}".format(error))
            resp.body = json.dumps({"message":"Failed to fetch data"})
            resp.status = falcon.HTTP_400

