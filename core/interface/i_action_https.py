from typing import *
from abc import ABC, abstractmethod

T = TypeVar("T")

class IActionHttps(ABC):
    @abstractmethod
    def _get(self, url: str, options: dict = {}) -> T:
        pass

    @abstractmethod
    def _post(self, url: str, options: dict = {}) -> T:
        pass

    @abstractmethod
    def _put(self, url: str, options: dict = {}) -> T:
        pass

    @abstractmethod
    def _delete(self, url: str, options: dict = {}) -> T:
        pass

    @abstractmethod
    def _patch(self, url: str, options: dict = {}) -> T:
        pass