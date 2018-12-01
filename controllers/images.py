import falcon
import json
from logger import set_up_logging
logger = set_up_logging()

class Resource(object):
    def on_get(self, req, resp):
        print("here i am")
        image_name = "testing image"
        logger.info("Image Server with image name : {}".format(image_name))
        doc = {
            'images': [
                {
                    'href': '/images/1eaf6ef1-7f2d-4ecc-a8d5-6e8adba7cc0e.png'
                }
            ]
        }

        # Create a JSON representation of the resource
        resp.body = json.dumps(doc, ensure_ascii=False)
        # The following line can be omitted because 200 is the default
        # status returned by the framework, but it is included here to
        # illustrate how this may be overridden as needed.
        resp.status = falcon.HTTP_200