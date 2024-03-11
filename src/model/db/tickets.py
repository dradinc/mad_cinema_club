import random
import string

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from src.modules.db import app_db
from src.model.db.users import UsersModel


class TicketsModel(app_db.Model):
    """
    Таблица для хранения билетов пользователей на сеансы фильмов.\n
    Билет не считается действительным без выданного номера билета (number), \n
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
    number = Column(String(10), nullable=True)
    # Внешний ключ с таблицей sessions
    sessions_id = Column(Integer, ForeignKey('sessions.id'))
    session = relationship('SessionsModel', back_populates='tickets')
    # Внешний ключ с таблицей rows_seats
    seat_id = Column(Integer, ForeignKey('rows_seats.id'))
    seat = relationship('RowsSeatsModel', back_populates='tickets')
    # Внешний ключ с таблицей users
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('UsersModel', back_populates='tickets')
    is_check = Column(Boolean, nullable=False, default=False)

    def __init__(self, session_id: int, seat_id: int, user_id: int):
        self.sessions_id = session_id
        self.seat_id = seat_id
        self.user_id = user_id

    def add_ticket(self):
        app_db.session.add(self)
        app_db.session.commit()

    @classmethod
    def del_ticket(cls, ticket_id):
        ticket = cls.query.filter(cls.id == ticket_id).first()
        app_db.session.delete(ticket)
        app_db.session.commit()

    @classmethod
    def pay_ticket(cls, session_id, current_user: UsersModel):
        tickets_list_for_session = []
        for ticket_user in current_user.tickets:
            if ticket_user.sessions_id == session_id:
                tickets_list_for_session.append(ticket_user)
        for ticket in tickets_list_for_session:
            if not ticket.number:
                ticket.generate_ticket_number()

    def generate_ticket_number(self):
        letters = string.ascii_uppercase
        digits = string.digits
        ticket_number = ''.join(random.choice(letters + digits) for _ in range(10))
        setattr(self, 'number', ticket_number)
        app_db.session.commit()

    @classmethod
    def get_user_tickets(cls, user_id):
        return cls.query.filter(cls.user_id == user_id, cls.number != None).all()

    def get_all_user_ticket_for_session(self):
        return TicketsModel.query.filter(TicketsModel.user_id == self.user_id, TicketsModel.number != None).all()

    @classmethod
    def get_ticket_use_number(cls, ticket_number: str):
        return cls.query.filter(cls.number == ticket_number).first()

    def check_ticket(self):
        setattr(self, 'is_check', True)
        app_db.session.commit()
