from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from src.modules.db import app_db


class FilmsModel(app_db.Model):
    """
    Таблица для хранения фильмов, которые показывают в кинотеатре.\n
    < id > - идентификатор фильма
    < title > - Название фильма
    < poster > - имя файла с постером фильма
    < genre > - список жанров фильма
    < trailers > - список трейлеров фильма
    < eng_title > - английское название фильма
    < god > - год производства фильма (выпуска)
    < country > - страна производства фильма
    < timing > - продолжительность фильма в минутах
    < age > - возрастное ограничение на фильм
    < review_title > - заголовок описания (может быть пустым)
    < review_text > - описание фильма
    """
    __tablename__ = 'films'

    # columns
    id = Column(Integer, primary_key=True)
    title = Column(String(64), nullable=False)
    poster = Column(String(32), nullable=False)
    genre = Column(String(256), nullable=False)
    trailers = Column(String(256), nullable=False)
    eng_title = Column(String(64), nullable=True)
    god = Column(String(4), nullable=False)
    country = Column(String(32), nullable=False)
    timing = Column(Integer, nullable=False)
    age = Column(String(3), nullable=False)
    review_title = Column(String(128), nullable=True)
    review_text = Column(String(512), nullable=False)
    # relationships
    sessions = relationship('SessionsModel', back_populates='film')

    @classmethod
    def get_films_for_main_page(cls):
        return cls.query.limit(5).all()

    @classmethod
    def get_all_films(cls):
        return cls.query.all()

    @classmethod
    def get_film_info(cls, film_id):
        return cls.query.filter(cls.id == film_id).first()
