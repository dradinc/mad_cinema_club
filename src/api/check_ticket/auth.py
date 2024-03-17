from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token
from flask_json import json_response

from src.model.db.users import UsersModel


class AuthCheckedApp(Resource):
    auth_checked_parser = reqparse.RequestParser()
    auth_checked_parser.add_argument(
        'login',
        type=str,
        help=''
    )
    auth_checked_parser.add_argument(
        'password',
        type=str,
        help=''
    )

    def post(self):
        request_args = self.auth_checked_parser.parse_args()
        if not request_args['login']:
            return json_response(
                status_=200,
                message='Аргумент \'login\' отсутствует или не заполнен'
            )
        elif not request_args['password']:
            return json_response(
                status_=200,
                message='Аргумент \'password\' отсутствует или не заполнен'
            )

        auth_user = UsersModel.find_user_by_email(request_args['login'])
        if auth_user:
            if auth_user.check_password(request_args["password"]):
                if not auth_user.is_checker:
                    return json_response(
                        status_=403,
                        message="Не достаточные права доступа"
                    )
                access_token = create_access_token(identity=auth_user.id)
                return json_response(
                    status_=200,
                    access_token=access_token
                )
            else:
                return json_response(
                    status_=400,
                    message='Не верный пароль'
                )
        else:
            return json_response(
                status_=400,
                message='Пользователя с данным логином не существует'
            )
