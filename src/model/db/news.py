from sqlalchemy import Column, Integer, String

from src.modules.db import app_db


class NewsModel(app_db.Model):
    """
    Очень простая таблица предназначенная просто для хранения новостей\n
    < id > - идентификатор новости \n
    < title > - заголовок новости \n
    < description > - краткое описание новости \n
    < image > - изображение (фон) новости
    """
    __tablename__ = 'news'

    # columns
    id = Column(Integer, primary_key=True)
    title = Column(String(32), nullable=False)
    description = Column(String(64), nullable=False)
    image = Column(String, nullable=False)

    @classmethod
    def get_news(cls):
        return cls.query.all()
