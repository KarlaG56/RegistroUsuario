from typing import Any
from abc import ABC, abstractmethod


class UserPort(ABC):
    @abstractmethod
    def update_verified_at(self, id: str) -> Any: pass

    @abstractmethod
    def register(self, name: str, lastname: str, cellphone: str, email: str, password: str) -> Any: pass

    @abstractmethod
    def search_user_by_token(self, token: str) -> Any: pass