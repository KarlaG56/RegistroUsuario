import string
import uuid

class User(object):
    def __init__(self, name:string, lastname:string,cellphone: string,email: string,password: string):
        self.id=str(uuid.uuid4())
        self._name = name
        self._lastname = lastname
        self._cellphone = cellphone
        self._email = email
        self._password = password
            

