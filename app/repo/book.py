from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Boolean

Base = declarative_base()

class Book(Base):
    __tablename__ = "book"
    isbn = Column(String, primary_key=True)
    title = Column(String)
    num_page = Column(Integer)
    in_print = Column(Boolean)