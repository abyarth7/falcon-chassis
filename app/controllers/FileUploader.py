import falcon
import json
from app.utils.db_connect import DBConnect
from logger import set_up_logging
from config.base import Session, engine, Base
from app.s3Services.botoFile import push_invoices_to_bucket

logger = set_up_logging()

# generate database schema
Base.metadata.create_all(engine)
# create a new session
session = Session()


class FileUploader(object):
    """Serves all apis related to Orders
    """

    def on_post(self, req, resp):
        try:
            push_invoices_to_bucket()
            logger.info("Order successfully placed.")
            doc = {"message": "Order successfully placed."}
            resp.body = json.dumps(doc)
            resp.status = falcon.HTTP_200
        except Exception as error:
            resp.body = json.dumps({"message": "Failed to place order"})
            logger.error("Failed to place order due to : {}".format(error))
            resp.status = falcon.HTTP_400
        session.commit()
        session.close()
