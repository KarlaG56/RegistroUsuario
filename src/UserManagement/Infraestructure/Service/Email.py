from UserManagement.Domain.Entity.User import User
from UserManagement.Infrestructure.Service.EmailPort import PortEmail

class Email(PortEmail):

    def run(self, user: User) -> None:
        try:
            pass
        except Exception:
            pass