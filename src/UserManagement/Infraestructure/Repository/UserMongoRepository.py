from datetime import datetime
from typing import Any

from src.UserManagement.Domain.Entity.User import User
from src.UserManagement.Infraestructure.Repository.Entity.UserMongoEntity import UserMongoEntity
from src.UserManagement.Domain.Port.PortUser import UserPort


class UserMongoRepository(UserPort):
    def __init__(self):
        self.user_model = UserMongoEntity

    def verify(self, user_id: str) -> Any:
        user_model = self.user_model.find_user({"uuid": user_id})
        if user_model:
            user_model['verified_at'] = datetime.now()
            self.user_model.update_user({"uuid": user_id}, {"$set": user_model})
        return user_model

    def create(self, name: str, lastname: str, cellphone: str, email: str, password: str) -> Any:
        user = User(name, lastname, cellphone, email, password)
        user_model = {
            "uuid": str(user.uuid),
            "name": user.name,
            "last_name": user.lastname,
            "cellphone": user.cellphone,
            "email": user.email,
            "password": user.password,
            "activation_token": user.token,
            "verified_at": user.activatedat
        }
        self.user_model.insert_user(user_model)
        return user

    def by_token(self, token: str) -> Any:
        return self.user_model.find_user({"token": token})

