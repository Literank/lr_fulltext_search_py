from dataclasses import asdict
from typing import List

from elasticsearch import Elasticsearch

from ...domain.gateway import BookManager
from ...domain.model import Book


INDEX_BOOK = "book_idx"


class ElasticSearchEngine(BookManager):
    def __init__(self, address: str, page_size: int):
        self.page_size = page_size
        self.client = Elasticsearch(address)

    def index_book(self, b: Book) -> str:
        result = self.client.index(index=INDEX_BOOK, document=asdict(b))
        return result['_id']

    def search_books(self, query: str) -> List[Book]:
        response = self.client.search(index=INDEX_BOOK, query={
            "multi_match": {
                "query": query,
                "fields": ["title", "author", "content"]
            }
        })
        return [hit["_source"] for hit in response["hits"]["hits"]]
