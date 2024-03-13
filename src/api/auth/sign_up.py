from random import randint

from flask_restful import Resource, reqparse
from flask_json import json_response
from flask_mail import Message

from src.modules.db import UsersModel
from src.modules.mail import app_mail


class SigUpSendCode(Resource):

    send_code = reqparse.RequestParser()
    send_code.add_argument(
        "email",
        type=str,
        help='User Email'
    )

    def post(self):
        # Получаем аргументы
        request_args = self.send_code.parse_args()

        # Проверяем все аргументы на наличие
        if not request_args['email']:
            return json_response(status_=400, message='Аргумент \'email\' отсутствует или не имеет данных')

        # Проверяем что пользователя с данным E-mail не существует или не закончил регистрацию
        check_users = UsersModel.find_user_by_email(email=request_args['email'])
        if check_users:
            if check_users.password:
                return json_response(
                    status_=400,
                    message='Пользователь с данным E-mail уже существует'
                )
        else:
            # Добавляем нового пользователя
            check_users = UsersModel(new_email=request_args['email'])
            check_users.add_new_user()

        # Генерируем новый код
        new_code = ''
        for i in range(6):
            new_code += str(randint(0, 9))

        # Добавляем код пользователю
        check_users.edit_user(**{'code': new_code})

        # Отправляем уведомление на почту
        message = Message('Код подтверждения', recipients=[request_args['email']])
        message.html = f"""
                    <p>Код подтверждения: %r</p>
                """ % new_code
        app_mail.send(message)

        return json_response(
            status_=200,
            message=f'Пароль отправлен на почту \'{request_args["email"]}\''
        )
