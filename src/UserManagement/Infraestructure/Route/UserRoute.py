from flask import Blueprint, request
from UserManagement.Infrestructure.Controller.RegisterUserController import RegistroUserController

user_blueprint = Blueprint('users', __name__)

@user_blueprint.route('/', methods=['POST'])
def register_user():
    data = request.get_json()
    return RegistroUserController.run(data)