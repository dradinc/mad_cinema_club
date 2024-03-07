from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from src.modules.db import app_db


class TicketsModel(app_db.Model):
    __tablename__ = 'tickets'

    # columns
    id = Column(Integer, primary_key=True)
    number = Column(String, nullable=True)
    # Внешний ключ с таблицей sessions
    sessions_id = Column(Integer, ForeignKey('sessions.id'))
    session = relationship('SessionsModel', back_populates='tickets')
    # Внешний ключ с таблицей rows_seats
    seat_id = Column(Integer, ForeignKey('rows_seats.id'))
    seat = relationship('RowsSeatsModel', back_populates='tickets')
    # Внешний ключ с таблицей users
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('UsersModel', back_populates='tickets')
