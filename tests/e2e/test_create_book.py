import http
import json
import unittest
import requests
import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Boolean

TITLE = "Testing all the Things"
NUM_PAGES = 340
ISBN = "123456789"


class CreateBookTest(unittest.TestCase):
    def test_something(self):
        db_url = os.getenv("DB_URL")
        # db_url = "postgresql+psycopg2://tester:testing@postgres/library"
        engine = create_engine(db_url)
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        Base = declarative_base()
        session = Session(engine)

        class TestBook(Base):
            __tablename__ = "book"
            isbn = Column(String, primary_key=True)
            title = Column(String)
            num_page = Column(Integer)
            in_print = Column(Boolean)

        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)
        r = requests.post("http://localhost:8000/book", json={"isbn": ISBN, "num_page": NUM_PAGES, "title": TITLE, "in_print": True})

        self.assertEqual(http.HTTPStatus.CREATED, r.status_code, r.text)

        j = json.loads(r.text)
        self.assertEqual(j["isbn"], ISBN)
        self.assertEqual(j["num_page"], NUM_PAGES)
        self.assertEqual(j["title"], TITLE)
        self.assertEqual(j["in_print"], True)

        try:
            book = session.query(TestBook).filter(TestBook.isbn == ISBN).one()
        except NoResultFound:
            self.fail("No book found with ISBN: %s" % ISBN)
            pass

        self.assertEqual(ISBN, book.isbn)
        self.assertEqual(TITLE, book.title)



if __name__ == '__main__':
    unittest.main()
