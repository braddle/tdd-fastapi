import http
import json
import unittest

import requests

from tests.base_db_test import BasedDBTest


class GetBookTest(BasedDBTest):
    def test_get_book_that_does_not_exists(self):
        r = requests.get("http://localhost:8000/book/123456789")

        self.assertEqual(http.HTTPStatus.NOT_FOUND, r.status_code)

        j = json.loads(r.text)

        self.assertEqual(j["detail"]["message"], "No book with isbn 123456789")


if __name__ == '__main__':
    unittest.main()
