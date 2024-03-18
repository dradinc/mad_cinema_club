from datetime import datetime

from flask_restful import Resource
from flask_json import json_response
from flask import request

from src.model.db.films.sessions import SessionsModel


class FilmSessions(Resource):

    def get(self, film_id):
        current_date = request.args.get('date')
        if not current_date:
            return json_response(
                status_=400,
                message='Аргумент \'date\' отсутствует или не имеет значения'
            )
        try:
            date = datetime.strptime(current_date, '%Y-%m-%d').date()
        except ValueError:
            return json_response(
                status_=400,
                message='Не верный формат даты: YYYY-MM-DD'
            )

        sessions_query = SessionsModel.get_sessions_for_films(film_id, date)
        cinema_list = []
        for session in sessions_query:
            is_continue = False

            # Проверяем есть ли кинотеатр в списке
            for cinema in cinema_list:
                if session.hall.cinema_id == cinema['id']:
                    # Если кинотеатр есть, то добавляем сессию и помечаем на продолжение
                    is_continue = True
                    cinema['sessions'].append({
                        'id': session.id,
                        'hall': session.hall.title,
                        'time': session.time.strftime('%H:%M'),
                        "cinema_type": session.cinema_type,
                        'price': session.price
                    })
                    break
            if is_continue:
                continue

            cinema_list.append({
                'id': session.hall.cinema_id,
                'title': session.hall.cinema.title,
                'latitude': session.hall.cinema.latitude,
                'longitude': session.hall.cinema.longitude,
                'sessions': [
                    {
                        'id': session.id,
                        'hall': session.hall.title,
                        'time': session.time.strftime('%H:%M'),
                        "cinema_type": session.cinema_type,
                        'price': session.price
                    }
                ]
            })

        return json_response(
            status_=200,
            cinema_list=cinema_list
        )
