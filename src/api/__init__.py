from flask_restful import Api
from flask_jwt_extended import JWTManager

from src import app


app_api = Api(app)
jwt_manager = JWTManager(app)

# Resource import
from src.api.test_request import TestRequest
from src.api.auth.sign_up import SignUp

# api endpoint
app_api.add_resource(TestRequest, '/api/test')
app_api.add_resource(SignUp, '/api/sign-up')
