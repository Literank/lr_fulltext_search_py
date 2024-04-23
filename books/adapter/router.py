import logging

from fastapi import FastAPI, HTTPException

from ..application.executor import BookOperator
from ..application import WireHelper
from ..domain.model import Book


class RestHandler:
    def __init__(self, logger: logging.Logger, book_operator: BookOperator):
        self._logger = logger
        self.book_operator = book_operator

    def create_book(self, b: Book):
        try:
            return self.book_operator.create_book(b)
        except Exception as e:
            self._logger.error(f"Failed to create: {e}")
            raise HTTPException(status_code=400, detail="Failed to create")


def make_router(app: FastAPI, wire_helper: WireHelper):
    rest_handler = RestHandler(
        logging.getLogger("lr-full-text"),
        BookOperator(wire_helper.book_manager())
    )

    @app.get("/")
    async def welcome():
        return {"status": "ok"}

    @app.post("/books")
    async def create_book(b: Book):
        book_id = rest_handler.create_book(b)
        return {"id": book_id}
