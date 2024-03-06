from flask_restful import Api

from src import app
from src.modules.jwt import app_jwt

app_api = Api(app)

# Resource import
from src.api.test_request import TestRequest, TestJwtRequest
from src.api.auth.sign_up import SignUp
from src.api.auth.sign_in import SignIn
from src.api.auth.forgot_password import SendCode, CheckCode, ResetPassword

# api endpoint
app_api.add_resource(TestRequest, '/api/test')
app_api.add_resource(TestJwtRequest, '/api/test-jwt')
app_api.add_resource(SignUp, '/api/sign-up')
app_api.add_resource(SignIn, '/api/sign-in')
app_api.add_resource(SendCode, '/api/forgot-password/send-code')
app_api.add_resource(CheckCode, '/api/forgot-password/check-code')
app_api.add_resource(ResetPassword, '/api/forgot-password/reset-password')
