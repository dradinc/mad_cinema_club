from flask_restful import Api
from flask_jwt_extended import JWTManager

from src import app


app_api = Api(app)
jwt_manager = JWTManager(app)

# Resource import
from src.api.test_request import TestRequest, TestJwtRequest
from src.api.auth.sign_up import SignUp
from  src.api.auth.sign_in import SignIn

# api endpoint
app_api.add_resource(TestRequest, '/api/test')
app_api.add_resource(TestJwtRequest, '/api/test-jwt')
app_api.add_resource(SignUp, '/api/sign-up')
app_api.add_resource(SignIn, '/api/sign-in')
