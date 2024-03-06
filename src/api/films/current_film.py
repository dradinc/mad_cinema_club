from flask_restful import Resource
from flask_json import json_response
from flask import url_for

from src.model.db.films import FilmsModel

from src import app


class CurrentFilm(Resource):

    def get(self, film_id):
        app.logger.info(film_id)

        current_film = FilmsModel.get_film_info(int(film_id))
        app.logger.info(current_film)

        if not current_film:
            return json_response(
                status_=404,
                message='Фильм не найден'
            )
        # Список жанров
        genre_list = []
        for genre in current_film.genre.split(';'):
            genre_list.append({
                'title': genre
            })
        # Список трейлеров
        trailer_list = []
        for trailer in current_film.trailers.split(';'):
            trailer_list.append({
                'trailer': url_for('static', filename=f'trailers/{trailer}')
            })

        return json_response(
            status_=200,
            film_info={
                "id": current_film.id,
                "title": current_film.title,
                "poster": url_for('static', filename=f'posters/{current_film.poster}'),
                "genre": genre_list,
                "trailers": trailer_list,
                "eng_title": current_film.eng_title,
                "god": current_film.god,
                "country": current_film.country,
                "timing": current_film.timing,
                "age": current_film.age,
                "review_title": current_film.review_title,
                "review_text": current_film.review_text
            }
        )
