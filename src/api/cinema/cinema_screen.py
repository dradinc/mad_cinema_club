from flask_restful import Resource
from flask_json import json_response

from src.model.db.cinema import CinemaModel


class CinemaScreen(Resource):

    def get(self):
        cinema_query = CinemaModel.get_all_cinema()
        cinema_list = []
        for cinema in cinema_query:
            cinema_list.append(
                {
                    'id': cinema.id,
                    'title': cinema.title,
                    'latitude': cinema.latitude,
                    'longitude': cinema.longitude
                }
            )

        return json_response(
            status_=200,
            cinema_list=cinema_list
        )
