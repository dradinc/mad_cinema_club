from flask_restful import Resource
from flask_json import json_response
from flask import url_for

from src.model.db.films import FilmsModel


class MainScreenFilms(Resource):

    def get(self):
        films_list_query = FilmsModel.get_films_for_main_page()
        film_list = []
        for film in films_list_query:
            genre_list = []
            for genre in film.genre.split(';'):
                genre_list.append(
                    {
                        'title': genre
                    }
                )
            film_list.append(
                {
                    'id': film.id,
                    'title': film.title,
                    'poster': url_for('static', filename=f'posters/{film.poster}'),
                    'genre': genre_list
                }
            )

        return json_response(
            status_=200,
            film_list=film_list
        )
