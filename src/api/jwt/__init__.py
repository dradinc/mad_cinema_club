from flask_jwt_extended import JWTManager

from src import app


app_jwt = JWTManager(app)
