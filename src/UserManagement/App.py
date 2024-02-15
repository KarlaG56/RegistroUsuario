from flask import Flask
from src.UserManagement.Infraestructure.Route.UserRoute import user_blueprint
from src.UserManagement.Infraestructure.Repository.Entity.UserSQLEntity import User

app = Flask(__name__)

app.register_blueprint(user_blueprint, url_prefix="/api/v1/users")

if __name__ == "__main__":
    app.run(debug=True)
