from flask_restful import Resource, reqparse
from flask_json import json_response
from flask_jwt_extended import jwt_required


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


class TestJwtRequest(Resource):

    @jwt_required()
    def get(self):  # simple GET access jwt
        return json_response(
            status_=200,
            message='GET JWT success request'
        )

    @jwt_required()
    def post(self):  # simple POST access jwt
        args = post_parser.parse_args()
        if not args['test']:
            return json_response(
                status_=400,
                message='Аргумент \'test\' пустой'
            )
        return json_response(
            status_=200,
            message=f'POST JWT success request, arg={args["test"]}'
        )

    @jwt_required()
    def put(self):  # simple PUT access jwt
        return json_response(
            status_=200,
            message='PUT JWT success request'
        )

    @jwt_required()
    def delete(self):  # simple DELETE access jwt
        return json_response(
            status_=200,
            message='DELETE JWT success request'
        )
