import unittest
import os
import warnings

from app.repo import book, book_repo

from tests.base_db_test import BasedDBTest


class MyTestCase(BasedDBTest):
    def test_creating_dublicate_book(self):
        warnings.filterwarnings("ignore")

        repo = book_repo.BookRepo(os.getenv("DB_URL"))
        b = book.Book()
        b.isbn = "98765432"
        b.title = "Testing Some Code"
        b.num_page = 1024
        b.in_print = True

        repo.create(b)
        # self.assertRaises(book_repo.DuplicateBook, repo.create(b))
        with self.assertRaises(book_repo.DuplicateBook):
            other = book.Book()
            other.isbn = "98765432"
            other.title = "Testing Some Other Code"
            other.num_page = 2048
            other.in_print = True
            repo.create(other)


if __name__ == '__main__':
    unittest.main()
