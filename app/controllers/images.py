import falcon
import json
from app.utils.db_connect import DBConnect
from logger import set_up_logging

logger = set_up_logging()
conn = DBConnect()


class Resource(object):
    def on_get(self, req, resp):
        try:
            image_name = "testing image"
            logger.info("Image Server with image name : {}".format(image_name))
            doc = {
                'images': [
                    {
                        'href': '/images/1eaf6ef1-7f2d-4ecc-a8d5-6e8adba7cc0e.png'
                    }
                ]
            }
            resp.body = json.dumps(doc)
            resp.status = falcon.HTTP_200
        except Exception as error:
            resp.body = json.dumps({'Error generated': error})
            resp.status = falcon.HTTP_400
        
        conn.close()

