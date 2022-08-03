from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from app.repo import book

class BookRepo:

    def __init__(self, db_url: str):
        self.engine = create_engine(db_url)
        # SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        # Base = declarative_base()
        self.session = Session(self.engine)

    def create(self, b: book.Book):
        self.session.add(b)
        self.session.commit()