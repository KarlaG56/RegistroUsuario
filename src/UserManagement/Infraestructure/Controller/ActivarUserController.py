from src.UserManagement.Application.UseCase.UserActivate import ActivateUserUseCase
from flask import jsonify


class ActivateUserController:
    def __init__(self, activarUseCase: ActivateUserUseCase):
        self.activarUseCase = activarUseCase

    def run(self, token):
        try:
            user = self.activarUseCase.run(token)
            return jsonify({"message": "User Validated", "Codigo": 201, "user": user}), 201
        except Exception as e:
            return jsonify({"Error": str(e), "Codigo": 500}), 500
