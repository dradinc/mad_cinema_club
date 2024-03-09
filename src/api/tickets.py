from datetime import datetime

from flask_restful import Resource
from flask_jwt_extended import jwt_required, current_user
from flask_json import json_response

from src.model.db.tickets import TicketsModel


class Tickets(Resource):

    @jwt_required()
    def get(self):
        tickets_query = TicketsModel.get_user_tickets(current_user.id)
        tickets_list = []

        for ticket in tickets_query:
            tickets_list.append({
                "id": ticket.id,
                "number": ticket.number,
                "cinema": {
                    "title": ticket.session.hall.cinema.title,
                    "coordinate": {
                        "latitude": ticket.session.hall.cinema.latitude,
                        "longitude": ticket.session.hall.cinema.longitude
                    }
                },
                "film": {
                    "id": ticket.session.film.id,
                    "title": ticket.session.film.title,
                    "genre": ", ".join(ticket.session.film.genre.split(';'))
                },
                "session_info": {
                    "hall": ticket.session.hall.title,
                    "row": ticket.seat.row,
                    "seat": ticket.seat.seat,
                    "time": ticket.session.time.strftime('%H:%M'),
                    "date": ticket.session.date.strftime('%d.%m.%Y')
                }
            })

        return json_response(
            status_=200,
            tickets_list=tickets_list
        )
