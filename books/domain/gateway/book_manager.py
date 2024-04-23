from abc import ABC, abstractmethod

from ..model import Book


class BookManager(ABC):
    @abstractmethod
    def index_book(self, b: Book) -> str:
        pass
