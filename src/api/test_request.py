from flask_restful import Resource
from flask_json import json_response


class TestRequest(Resource):

    def get(self):
        return json_response(
            status_=200,
            message='GET success request'
        )

    def post(self):
        return json_response(
            status_=200,
            message='POST success request'
        )

    def put(self):
        return json_response(
            status_=200,
            message='PUT success request'
        )

    def delete(self):
        return json_response(
            status_=200,
            message='DELETE success request'
        )
