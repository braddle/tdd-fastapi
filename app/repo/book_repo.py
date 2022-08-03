from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.repo import book

class BookRepo:

    def __init__(self, db_url: str):
        self.engine = create_engine(db_url)
        self.session = Session(self.engine)

    def create(self, b: book.Book):
        try:
            self.session.add(b)
            self.session.commit()
        except IntegrityError:
            raise DuplicateBook("testing")


class DuplicateBook(Exception):
    pass