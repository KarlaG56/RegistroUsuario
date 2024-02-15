from datetime import datetime
from src.Database.SQL import SessionLocal
from typing import Any
from src.UserManagement.Domain.Port.PortUser import UserPort
from src.UserManagement.Domain.Entity.User import User
from src.UserManagement.Infraestructure.Repository.Entity.UserMySQLEntity import User as Entidad


class UserMySQLRepository(UserPort):
    def __init__(self):
        self.session = SessionLocal

    def register(self, name: str, lastname: str, cellphone: str, email: str, password: str) -> Any:
        user = User(name, lastname, cellphone, email, password)
        entidad = Entidad(uuid=str(user.uuid), name=user.name, last_name=user.last_name, cellphone=user.cellphone,
                          email=user.email, password=user.password, activation_token=user.activation_token,
                          verified_at=user.activated_at)
        self.session.add(entidad)
        self.session.commit()
        return user

    def search_user_by_token(self, token: str) -> Any:
        return self.session.query(Entidad).filter(Entidad.activation_token == token).first

    def update_verified_at(self, id: str) -> Any:
        user_model = self.session.query(Entidad).filter(Entidad.uuid == id).first()
        user_model.verified_at = datetime.now()
        response = {"uuid": str(user_model.uuid),
                    "name": user_model.name,
                    "last_name": user_model.last_name,
                    "email": user_model.email,
                    "cellphone": user_model.cellphone,
                    "activated_at": str(user_model.verified_at)
                    }
        self.session.commit()
        return response
