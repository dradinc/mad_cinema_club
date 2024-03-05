from flask_restful import Resource, reqparse
from flask_json import json_response

from src.model.db.users import UsersModel

sign_up_parse = reqparse.RequestParser()
sign_up_parse.add_argument(
    'name',
    type=str,
    help='User name'
)
sign_up_parse.add_argument(
    'email',
    type=str,
    help='User email'
)
sign_up_parse.add_argument(
    'password',
    type=str,
    help='User password'
)


class SignUp(Resource):

    def post(self):
        # Получаем аргументы
        request_args = sign_up_parse.parse_args()

        # Проверяем что все аргументы имеют значения (не пустые)
        if not request_args['name']:
            return json_response(
                status_=400,
                message=f'Аргумент \'name\' не содержит значений'
            )
        elif not request_args['email']:
            return json_response(
                status_=400,
                message=f'Аргумент \'email\' не содержит значений'
            )
        elif not request_args['password']:
            return json_response(
                status_=400,
                message=f'Аргумент \'password\' не содержит значений'
            )

        # Создаем нового пользователя
        new_user = UsersModel(**request_args)
        new_user.add_new_user()

        return json_response(
            status_=200,
            message='Пользователь успешно создан'
        )
