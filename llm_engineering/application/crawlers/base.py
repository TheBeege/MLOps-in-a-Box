import time
from abc import ABC, abstractmethod
from tempfile import mkdtemp

from llm_engineering.domain.documents import NoSQLBaseDocument


class BaseCrawler(ABC):
    model: type[NoSQLBaseDocument]

    @abstractmethod
    def extract(self, link: str, **kwargs) -> None: ...
