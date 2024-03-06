from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from src.modules.db import app_db


class FilmsModel(app_db.Model):
    __tablename__ = 'films'

    # columns
    id = Column(Integer, primary_key=True)
    title = Column(String(64), nullable=False)
    poster = Column(String(32), nullable=False)
    genre = Column(String, nullable=False)
    trailers = Column(String, nullable=False)
    eng_title = Column(String(64), nullable=True)
    god = Column(String(4), nullable=False)
    country = Column(String(32), nullable=False)
    timing = Column(Integer, nullable=False)
    age = Column(String(3), nullable=False)
    review_title = Column(String(128), nullable=True)
    review_text = Column(String, nullable=False)
    # relationships
    sessions = relationship('SessionsModel', back_populates='film')

    @classmethod
    def get_films_for_main_page(cls):
        return cls.query.limit(5).all()

    @classmethod
    def get_film_info(cls, film_id):
        return cls.query.filter(cls.id == film_id).first()
