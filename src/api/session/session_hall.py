from flask_restful import Resource, reqparse
from flask_json import json_response
from flask_jwt_extended import jwt_required, current_user

from src.model.db.films.sessions import SessionsModel
from src.model.db.tickets import TicketsModel


session_hall_parser = reqparse.RequestParser()
session_hall_parser.add_argument(
    'seat_id',
    type=int,
    help='Integer seat_id'
)


class SessionHall(Resource):

    def get(self, session_id):
        current_session = SessionsModel.get_session(session_id)
        scheme = current_session.get_hall_scheme()
        return json_response(
            status_=200,
            scheme=scheme
        )

    @jwt_required()
    def post(self, session_id: int):
        request_args = session_hall_parser.parse_args()
        if not request_args['seat_id']:
            return json_response(
                status_=400,
                message='Аргумент \'seat_id\' отсутствует или не имеет значения'
            )
        result = SessionsModel.select_seat(session_id, current_user.id, request_args['seat_id'])
        if result:
            return json_response(status_=200)
        else:
            return json_response(status_=409, message='Выбранное место уже занято :(')

    @jwt_required()
    def put(self, session_id: int):
        TicketsModel.pay_ticket(session_id, current_user)
        return json_response(status_=200)

