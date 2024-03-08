from flask_restful import Resource
from flask_json import json_response

from src.model.db.films.sessions import SessionsModel


class SessionHall(Resource):

    def get(self, session_id):
        current_session = SessionsModel.get_session(session_id)
        scheme = current_session.get_hall_scheme()
        return json_response(
            status_=200,
            scheme=scheme
        )
