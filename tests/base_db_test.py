import unittest

import os

from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Boolean

db_url = os.getenv("DB_URL")
engine = create_engine(db_url)
Base = declarative_base()

class BasedDBTest(unittest.TestCase):

    def setUp(self):
        self.session = Session(engine)
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)

    def tearDown(self):
        self.session.close()
        pass


class TestBook(Base):
    __tablename__ = "book"
    isbn = Column(String, primary_key=True)
    title = Column(String)
    num_page = Column(Integer)
    in_print = Column(Boolean)

TestBook.__test__ = False