from flask_restful import Api
from flask_jwt_extended import JWTManager

from src import app


app_api = Api(app)
jwt_manager = JWTManager(app)

# Resource import
from src.api.test_request import TestRequest

# api endpoint
app_api.add_resource(TestRequest, '/api/test')
