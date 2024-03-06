from flask_restful import Resource
from flask_json import json_response
from flask import url_for

from src.model.db.news import NewsModel


class News(Resource):

    def get(self):
        news_query = NewsModel.get_news()
        news_list = []
        for news in news_query:
            news_list.append(
                {
                    'title': news.title,
                    'description': news.description,
                    'image': url_for('static', filename=f'news/{news.image}')
                }
            )

        return json_response(
            status_=200,
            news_list=news_list
        )
