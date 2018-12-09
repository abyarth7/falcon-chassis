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


class GetOrderDetails(object):
    """Serves all apis related to Orders
    """

    def on_get(self, req, resp):
        try:
            cart_order = session.query(OrderCart).filter_by(id=6).all()
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

    # def on_post(self, req, resp):
    #     try:
    #         cart_order_data = OrderCart(patient_id=426)
    #         order_detail_data = OrderDetails(order_type="Profile")
    #         order_detail_data2 = OrderDetails(order_type="Test")
    #         order_address = PickupAddress(house_no='No.92', street='3rd Cross Road',
    #                                       area='7th Block', city='Bengaluru', state='Karnataka', pincode=769019)
    #         order_payment = PaymentDetails(discount='20', wallet_credits='20', promo_code='NDSCFV',
    #                                        order_net_price=100, total_billed_amount=100, balance_payable=150)
    #         phlebo_data = PhleboDetails(
    #             phlebo_id=1, phlebo_name='Susui', phlebo_phone='8763')
    #         cart_order_data.phlebo_detail = phlebo_data
    #         cart_order_data.order_detail = [
    #             order_detail_data, order_detail_data2]
    #         cart_order_data.pickup_address = order_address
    #         cart_order_data.payment_detail = order_payment
    #         session.add(cart_order_data)

    #         logger.info("Order successfully placed.")
    #         doc = {"message": "Order successfully placed."}
    #         resp.body = json.dumps(doc)
    #         resp.status = falcon.HTTP_200
    #     except Exception as error:
    #         resp.body = json.dumps({'Error generated': error})
    #         resp.status = falcon.HTTP_400
    #     session.commit()
    #     session.close()
