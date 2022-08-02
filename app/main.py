import http

import sqlalchemy
from fastapi import FastAPI
from pydantic import BaseModel

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Boolean

app = FastAPI()

db_url = "postgresql+psycopg2://tester:testing@postgres/library"
engine = create_engine(db_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
session = Session(engine)


class BaseBook(BaseModel):
    isbn: str
    title: str
    num_page: int
    in_print: bool


class TestBook(Base):
    __tablename__ = "book"
    isbn = Column(String, primary_key=True)
    title = Column(String)
    num_page = Column(Integer)
    in_print = Column(Boolean)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/health")
async def check_health():
    return {"status": "OK"}


@app.post("/book", status_code=http.HTTPStatus.CREATED)
async def create_book(bb: BaseBook):
    tb = TestBook()
    tb.isbn = bb.isbn
    tb.title = bb.title
    tb.num_page = bb.num_page
    tb.in_print = bb.in_print

    session.add(tb)
    session.commit()

    return bb
