from ...domain.model import Book
from ...domain.gateway import BookManager


class BookOperator():

    def __init__(self, book_manager: BookManager):
        self.book_manager = book_manager

    def create_book(self, b: Book) -> str:
        return self.book_manager.index_book(b)
