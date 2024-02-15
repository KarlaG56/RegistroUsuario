from typing import Any
from abc import ABC, abstractmethod


class UserPort(ABC):
    @abstractmethod
    def verify(self, id: str) -> Any: pass

    @abstractmethod
    def create(self, name: str, lastname: str, cellphone: str, email: str, password: str) -> Any: pass

    @abstractmethod
    def by_token(self, token: str) -> Any: pass