from ..domain.gateway import BookManager
from ..infrastructure.config import Config
from ..infrastructure.search import ElasticSearchEngine


class WireHelper:
    def __init__(self, engine: ElasticSearchEngine):
        self.engine = engine

    @classmethod
    def new(cls, c: Config):
        es = ElasticSearchEngine(
            c.search.address, c.search.index, c.app.page_size)
        return cls(es)

    def book_manager(self) -> BookManager:
        return self.engine
