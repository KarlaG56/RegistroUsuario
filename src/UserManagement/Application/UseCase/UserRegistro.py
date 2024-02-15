from typing import Union
from src.UserManagement.Domain.Entity.User import User
from src.UserManagement.Domain.Port.PortUser import UserPort


class RegisterUserUseCase:
    def __init__(self, repository: UserPort):
        self.repository = repository

    def run(self, name, lastname, cellphone, email, password) -> Union[User, None]:
        try:
            return self.repository.register(name, lastname, cellphone, email, password)
        except Exception:
            return None
