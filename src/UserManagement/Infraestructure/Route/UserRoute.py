from flask import Blueprint, request
from src.UserManagement.Infraestructure.Controller.RegistroUserController import RegisterUserController
from src.UserManagement.Infraestructure.Controller.ActivarUserController import ActivateUserController
from src.UserManagement.Application.UseCase.UserRegistro import RegisterUserUseCase
from src.UserManagement.Application.UseCase.UserActivate import ActivateUserUseCase
from src.UserManagement.Infraestructure.Repository.UserMySQLRepository import UserMySQLRepository
from src.UserManagement.Infraestructure.Repository.UserMySQLRepository import User

user_blueprint = Blueprint('users', __name__)
repository = UserMySQLRepository
registroUserUseCase = RegisterUserUseCase(repository)
registroUserController = RegisterUserController(registroUserUseCase)
activarUserUseCase = ActivateUserUseCase(repository)
activarUserController = ActivateUserController(activarUserUseCase)



@user_blueprint.route('/', methods=['POST'])
def register_user():
    data = request.get_json()
    return registroUserController.run(data)

@user_blueprint.route('/<token>/active', methods=['PUT'])
def activate(token):
    return activarUserController.run(token)
