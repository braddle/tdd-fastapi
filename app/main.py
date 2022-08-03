import http
import os

from fastapi import FastAPI, Depends
from pydantic import BaseModel

from app.repo import book_repo, book

app = FastAPI()


class BaseBook(BaseModel):
    isbn: str
    title: str
    num_page: int
    in_print: bool


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/health")
async def check_health():
    return {"status": "OK"}


def create_repo():
    return book_repo.BookRepo(os.getenv("DB_URL"))


@app.post("/book", status_code=http.HTTPStatus.CREATED)
async def create_book(bb: BaseBook, repo = Depends(create_repo)):
    b = book.Book()
    b.title = bb.title
    b.isbn = bb.isbn
    b.num_page = bb.num_page
    b.in_print = bb.in_print

    repo.create(b)

    return bb
