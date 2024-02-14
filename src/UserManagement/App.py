from flask import Flask
from src.UserManagement.Infraestructure.Route.UserRoute import user_blueprint
from src.Database.SQL import crear

app = Flask(__name__)

app.register_blueprint(user_blueprint, url_prefix="/api/v1/users")

crear()

if __name__ == "__main__":
    app.run(debug=True)
