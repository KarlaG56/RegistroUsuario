from datetime import datetime
from src.Database.SQLite import SessionLocal
from typing import Any
from src.UserManagement.Domain.Port.PortUser import UserPort
from src.UserManagement.Domain.Entity.User import User
from src.UserManagement.Infraestructure.Repository.Entity.UserSQLEntity import User as Entidad


class UserSQLiteRepository(UserPort):
    def __init__(self):
        self.session = SessionLocal

    def create(self, name: str, lastname: str, cellphone: str, email: str, password: str) -> Any:
        user = User(name, lastname, cellphone, email, password)
        entidad = Entidad(uuid=str(user.uuid), name=user.name, lastname=user.lastname, cellphone=user.cellphone,
                          email=user.email, password=user.password, token=user.token,
                          verified_at=user.activated_at)
        self.session.add(entidad)
        self.session.commit()
        return user

    def by_token(self, token: str) -> Any:
        return self.session.query(Entidad).filter(Entidad.token == token).first

    def verify(self, id: str) -> Any:
        user_model = self.session.query(Entidad).filter(Entidad.uuid == id).first()
        user_model.verified_at = datetime.now()
        response = {"uuid": str(user_model.uuid),
                    "name": user_model.name,
                    "last_name": user_model.lastname,
                    "email": user_model.email,
                    "cellphone": user_model.cellphone,
                    "activated_at": str(user_model.verifiedat)
                    }
        self.session.commit()
        return response
