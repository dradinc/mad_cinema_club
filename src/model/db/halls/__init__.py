from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from src.modules.db import app_db


class HallsModel(app_db.Model):
    """
    Таблица хранящая в себе информацию о залах для кинотеатров
    К залам присоединяются схемы залов (что позволяет использовать одни схемы для разных кинотеатров)
    И залы после присоединяются к кинотеатрам, что помогает сессии получить информацию по кинотеатру\n
    < id > - идентификатор зала\n
    < title > - наименование зала\n
    < cinema_id > - кинотеатр, к которому принадлежит зал\n
    < scheme_id > - схема расположения мест в зале
    """
    __tablename__ = 'halls'

    # column
    id = Column(Integer, primary_key=True)
    title = Column(String(16), nullable=False)
    # cinema relationship
    cinema_id = Column(Integer, ForeignKey('cinema.id'))
    cinema = relationship('CinemaModel', back_populates='halls')
    # scheme relationship
    scheme_id = Column(Integer, ForeignKey('hall_scheme.id'))
    scheme = relationship('SchemeModel', back_populates='halls')
    # relationships
    sessions = relationship('SessionsModel', back_populates='hall')
