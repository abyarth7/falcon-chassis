from settings import DB_URL 
from sqlalchemy import create_engine
from logger import set_up_logging
logger = set_up_logging()

engine = create_engine(DB_URL, pool_size=5, max_overflow=10)

connection = engine.connect()
result = connection.execute("select name from company")

if result:
    logger.info("Attempting to connect to database status : {}".format("SUCCESS"))
    print("connection made with humanity")
else:
    logger.critical("Attempting to connect to database status : {}".format("FAILED"))
    print("failed to connect")

for row in result:
    print("username:", row['name'])
connection.close()