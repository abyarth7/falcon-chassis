from settings import DB_URL 
from sqlalchemy import create_engine

class DBConnect():
    def __init__(self):
        self.engine = create_engine(DB_URL, pool_size=5, max_overflow=10)
        self.cur = self.engine.connect()

    def query(self, query):
        result = self.cur.execute(query)
        return result

    def close(self):
        self.cur.close()
