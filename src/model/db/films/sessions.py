import datetime

from sqlalchemy import Column, Integer, Date, Time, String, ForeignKey
from sqlalchemy.orm import relationship

from src.modules.db import app_db


class SessionsModel(app_db.Model):
    __tablename__ = 'sessions'

    # column
    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    time = Column(Time, nullable=False)
    price = Column(Integer, nullable=False)
    cinema_type = Column(String(2), nullable=False, default='2D')
    # film relationship
    film_id = Column(Integer, ForeignKey('films.id'))
    film = relationship('FilmsModel', back_populates='sessions')
    # hall relationship
    hall_id = Column(Integer, ForeignKey('halls.id'))
    hall = relationship('HallsModel', back_populates='sessions')

    @classmethod
    def get_sessions_for_cinema(cls, cinema_id, date: datetime.date):
        all_list = cls.query.order_by(cls.time).all()
        request_list = []
        for item in all_list:
            if item.hall.cinema_id == int(cinema_id) and item.date == date:
                request_list.append(item)
        return request_list

    @classmethod
    def get_sessions_for_films(cls, film_id, date: datetime.date):
        all_list = cls.query.order_by(cls.time).all()
        request_list = []
        for item in all_list:
            if item.film_id == int(film_id) and item.date == date:
                request_list.append(item)
        return request_list
