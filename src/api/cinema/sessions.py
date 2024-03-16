from datetime import datetime

from flask_restful import Resource, reqparse
from flask_json import json_response
from flask import url_for

from src.model.db.films.sessions import SessionsModel


class CinemaSessions(Resource):
    cinema_session_parser = reqparse.RequestParser()
    cinema_session_parser.add_argument(
        'date',
        type=str,
        help='Date sessions'
    )

    def get(self, cinema_id):
        request_args = self.cinema_session_parser.parse_args()
        if not request_args['date']:
            return json_response(
                status_=400,
                message='Аргумент \'date\' отсутствует или является пустым'
            )
        try:
            date = datetime.strptime(request_args['date'], '%Y-%m-%d').date()
        except ValueError:
            return json_response(
                status_=400,
                message='Не верный формат даты: YYYY-MM-DD'
            )

        # Получаем список сессий
        sessions_query = SessionsModel.get_sessions_for_cinema(cinema_id, date)

        films_list = []
        for session in sessions_query:
            is_continue = False

            # Проверяем есть ли фильм уже в списке
            for film in films_list:
                if session.film.id == film['id']:
                    # Если фильм есть, то помечаем, что его не нужно будет добавлять
                    is_continue = True
                    film['sessions'].append({
                        'id': session.id,
                        'hall': session.hall.title,
                        'time': session.time.strftime('%H:%M'),
                        "cinema_type": session.cinema_type,
                        'price': session.price
                    })
                    break
            if is_continue:
                continue

            # Если фильм нет, то добавляем его
            genre_list = []
            for genre in session.film.genre.split(';'):
                genre_list.append(
                    {
                        'title': genre
                    }
                )
            films_list.append({
                'id': session.film.id,
                'poster': url_for('static', filename=f'poster/{session.film.poster}'),
                'title': session.film.title,
                'timing': session.film.timing,
                'age': session.film.age,
                'genre': genre_list,
                'sessions': [{
                    'id': session.id,
                    'hall': session.hall.title,
                    'time': session.time.strftime('%H:%M'),
                    "cinema_type": session.cinema_type,
                    'price': session.price
                }]
            })

        return json_response(
            status_=200,
            films_list=films_list
        )
