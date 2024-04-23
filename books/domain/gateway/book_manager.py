from abc import ABC, abstractmethod
from typing import List

from ..model import Book


class BookManager(ABC):
    @abstractmethod
    def index_book(self, b: Book) -> str:
        pass

    @abstractmethod
    def search_books(self, query: str) -> List[Book]:
        pass
