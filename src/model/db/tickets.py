from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from src.modules.db import app_db


class TicketsModel(app_db.Model):
    """
    Таблица для хранения билетов пользователей на сеансы фильмов.\n
    Билет не считается действительным без выданного номера билета (number),\n
    До тех пор он считается просто забронированным местом.\n
    < id > - идентификатор билета\n
    < number > - номер билета\n
    < session_id > - сеанс, действующий для билета\n
    < seat_id > - место в зале (идет проверка чтобы зал места совпадал с залом сеанса)\n
    < user_id > - пользователь, который забронировал/приобрел билеты\n
    """
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
