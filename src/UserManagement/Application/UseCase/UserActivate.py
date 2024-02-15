from typing import Union
from src.UserManagement.Domain.Entity.User import User
from src.UserManagement.Domain.Port.PortUser import UserPort

class ActivateUserUseCase:
    def __init__(self, repository: UserPort):
        self.repository = repository

    def run(self, token: str) -> Union[User, None]:
        try:
            return self.repository.verify(self.repository.by_token(token).id)
        except Exception as e:
            pass