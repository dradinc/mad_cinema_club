from flask_restful import Resource, reqparse
from flask_json import json_response


# POST parser
post_parser = reqparse.RequestParser()  # Переменная для работы с данными
post_parser.add_argument(  # Добавление аргумента
    'test',
    type=str,
    help='Тестовый аргумент'
)


class TestRequest(Resource):

    def get(self):  # simple GET
        return json_response(
            status_=200,
            message='GET success request'
        )

    def post(self):  # simple POST
        args = post_parser.parse_args()
        if not args['test']:
            return json_response(
                status_=400,
                message='Аргумент \'test\' пустой'
            )
        return json_response(
            status_=200,
            message=f'POST success request, arg={args["test"]}'
        )

    def put(self):  # simple PUT
        return json_response(
            status_=200,
            message='PUT success request'
        )

    def delete(self):  # simple DELETE
        return json_response(
            status_=200,
            message='DELETE success request'
        )
