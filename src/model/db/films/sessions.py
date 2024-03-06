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
