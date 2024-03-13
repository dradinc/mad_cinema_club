from flask_restful import Resource, reqparse
from flask_json import json_response
from flask_jwt_extended import create_access_token

from src.modules.db import UsersModel

sign_in_parse = reqparse.RequestParser()
sign_in_parse.add_argument(
    'email',
    type=str,
    help='User email'
)
sign_in_parse.add_argument(
    'password',
    type=str,
    help='User password'
)


class SignIn(Resource):

    def post(self):
        request_args = sign_in_parse.parse_args()

        if not request_args['email']:
            return json_response(
                status_=400,
                message=f'Аргумент \'email\' отсутствует или не содержит значений'
            )
        elif not request_args['password']:
            return json_response(
                status_=400,
                message=f'Аргумент \'password\' отсутствует или не содержит значений'
            )

        auth_user = UsersModel.find_user_by_email(request_args['email'])
        if auth_user:
            if not auth_user.password:
                return json_response(status_=400, message=f'Пользователь не закончил регистрацию!')
            if auth_user.check_password(request_args["password"]):
                access_token = create_access_token(identity=auth_user.id)

                user_info = {
                    "name": auth_user.name,
                    "email": auth_user.email,
                    "balance": auth_user.balance
                }

                return json_response(
                    status_=200,
                    access_token=access_token,
                    user_info=user_info
                )
            else:
                return json_response(
                    status_=400,
                    message='Не верный пароль'
                )
        else:
            return json_response(
                status_=400,
                message='Пользователя с данным E-mail не существует'
            )
