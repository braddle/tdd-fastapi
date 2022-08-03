import http
import json
import unittest

import requests

from sqlalchemy.exc import NoResultFound

from tests.base_db_test import BasedDBTest, TestBook

TITLE = "Testing all the Things"
NUM_PAGES = 340
ISBN = "123456789"

class CreateBookTest(BasedDBTest):
    def test_something(self):
        r = requests.post("http://localhost:8000/book", json={"isbn": ISBN, "num_page": NUM_PAGES, "title": TITLE, "in_print": True})

        self.assertEqual(http.HTTPStatus.CREATED, r.status_code, r.text)

        j = json.loads(r.text)
        self.assertEqual(j["isbn"], ISBN)
        self.assertEqual(j["num_page"], NUM_PAGES)
        self.assertEqual(j["title"], TITLE)
        self.assertEqual(j["in_print"], True)

        try:
            book = self.session.query(TestBook).filter(TestBook.isbn == ISBN).one()
        except NoResultFound:
            self.fail("No book found with ISBN: %s" % ISBN)
            pass

        self.assertEqual(ISBN, book.isbn)
        self.assertEqual(TITLE, book.title)


if __name__ == '__main__':
    unittest.main()
