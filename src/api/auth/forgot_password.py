from random import randint

from flask_restful import Resource, reqparse
from flask_json import json_response
from flask_mail import Message

from src.modules.db import UsersModel
from src.modules.mail import app_mail


send_code_parse = reqparse.RequestParser()
send_code_parse.add_argument(
    'email',
    type=str,
    help='User email'
)

check_code_parse = reqparse.RequestParser()
check_code_parse.add_argument(
    'email',
    type=str,
    help='User email'
)
check_code_parse.add_argument(
    'code',
    type=str,
    help='User verify code'
)

reset_password_pars = reqparse.RequestParser()
reset_password_pars.add_argument(
    'email',
    type=str,
    help='User email'
)
reset_password_pars.add_argument(
    'code',
    type=str,
    help='User verify code'
)
reset_password_pars.add_argument(
    'new_password',
    type=str,
    help='New user password'
)


class SendCode(Resource):

    def post(self):
        request_args = send_code_parse.parse_args()

        if not request_args['email']:
            return json_response(
                status_=400,
                message=f'Аргумент \'email\' отсутствует или не содержит значений'
            )

        user = UsersModel.find_user_by_email(request_args['email'])
        if user:
            # Генерируем новый код
            new_code = ''
            for i in range(6):
                new_code += str(randint(0, 9))

            # Добавляем код пользователю
            user.edit_user(**{'code': new_code})

            # Отправляем уведомление на почту
            message = Message('Код подтверждения', recipients=[request_args['email']])
            message.html = f"""
                <p>Код подтверждения: %r</p>
            """ % new_code
            app_mail.send(message)

            return json_response(
                status_=200,
                message=f'Код отправлен на почту {request_args["email"]}'
            )
        else:
            return json_response(
                status_=400,
                message=f'Пользователя с данным E-mail не существует'
            )


class CheckCode(Resource):

    def post(self):
        request_args = check_code_parse.parse_args()

        if not request_args['email']:
            return json_response(
                status_=400,
                message=f'Аргумент \'email\' отсутствует или не содержит значений'
            )
        elif not request_args['code']:
            return json_response(
                status_=400,
                message=f'Аргумент \'code\' отсутствует или не содержит значений'
            )

        check_user = UsersModel.find_user_by_email(request_args['email'])
        if check_user.code == request_args['code']:
            return json_response(
                status_=200
            )
        else:
            return json_response(
                status_=412,
                message='Не верный код'
            )


class ResetPassword(Resource):

    def post(self):
        request_args = reset_password_pars.parse_args()

        if not request_args['email']:
            return json_response(
                status_=400,
                message=f'Аргумент \'email\' отсутствует или не содержит значений'
            )
        elif not request_args['code']:
            return json_response(
                status_=400,
                message=f'Аргумент \'code\' отсутствует или не содержит значений'
            )
        elif not request_args['new_password']:
            return json_response(
                status_=400,
                message=f'Аргумент \'new_password\' отсутствует или не содержит значений'
            )

        check_user = UsersModel.find_user_by_email(request_args['email'])
        if check_user.code == request_args['code']:
            check_user.edit_user(**{
                'password': request_args['new_password'],
                'code': ""
            })
            return json_response(
                status_=200,
                message="Пароль успешно изменен"
            )
        else:
            return json_response(
                status_=412,
                message='Не верный код'
            )
