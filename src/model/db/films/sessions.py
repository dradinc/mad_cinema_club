import datetime

from sqlalchemy import Column, Integer, Date, Time, String, ForeignKey
from sqlalchemy.orm import relationship

from src.modules.db import app_db
from src.model.db.tickets import TicketsModel


class SessionsModel(app_db.Model):
    """
    Таблица предназначена для хранения информации по сеансам разных фильмов в разных залах=>кинотеатрах\n
    < id > - первичный ключ\n
    < date > - дата проведения сеанса\n
    < time > - время назначено начала сеанса\n
    < price > - стоимость билета на сеанс\n
    < cinema_type > - формат фильма (2D или 3D)\n
    < film_id > - фильм на сеансе\n
    < hall_id > - зал для сеанса (оттуда же берется кинотеатр)
    """
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
    # relationships
    tickets = relationship('TicketsModel', back_populates='session')

    @classmethod
    def get_sessions_for_cinema(cls, cinema_id, date: datetime.date):
        """
        Возвращает список сессий для кинотеатра включая все фильмы, которые в нем показывают
        :param cinema_id:
        :param date:
        :return:
        """
        all_list = cls.query.order_by(cls.time).all()
        request_list = []
        for item in all_list:
            if item.hall.cinema_id == int(cinema_id) and item.date == date:
                request_list.append(item)
        return request_list

    @classmethod
    def get_sessions_for_films(cls, film_id, date: datetime.date):
        """
        Возвращает список сессий для фильма включая все кинотеатры
        :param film_id:
        :param date:
        :return:
        """
        all_list = cls.query.order_by(cls.time).all()
        request_list = []
        for item in all_list:
            if item.film_id == int(film_id) and item.date == date:
                request_list.append(item)
        return request_list

    @classmethod
    def get_session(cls, session_id: int):
        return cls.query.filter(cls.id == session_id).first()

    def get_hall_scheme(self):
        scheme = []
        for seat in self.hall.scheme.rows_seats:
            is_continue = False

            seat_state = False
            for ticket in self.tickets:
                if seat.id == ticket.seat_id:
                    seat_state = True
                    break

            for item in scheme:
                if item['row'] == seat.row:
                    item['seats'].append({
                        'id': seat.id,
                        'is_empty': seat.is_empty,
                        'reservation': seat_state
                    })
                    is_continue = True
                    break

            if is_continue:
                continue

            scheme.append({
                'row': seat.row,
                'seats': [{
                    'id': seat.id,
                    'is_empty': seat.is_empty,
                    'reservation': seat_state
                }]
            })
        return scheme

    @classmethod
    def select_seat(cls, session_id: int, user_id: int, seat_id: int):
        current_session = cls.get_session(session_id)
        for ticket in current_session.tickets:
            if ticket.seat_id == seat_id:
                if not ticket.number:
                    if ticket.user_id == user_id:
                        TicketsModel.del_ticket(ticket.id)
                        return True
                return False
        ticket = TicketsModel(session_id, seat_id, user_id)
        ticket.add_ticket()
        return True
