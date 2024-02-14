from typing import Union
from UserManagement.Domain.Entity.User import User
from UserManagement.Domain.Port.UserPort import PortUser

class ActivateUserUseCase:
    def __init__(self, repository: PortUser):
        self.repository = repository

    def run(self, token: str) -> Union[User, None]:
        try:
            return self.repository.search_user_by_token(token)
        except Exception as e:
            pass