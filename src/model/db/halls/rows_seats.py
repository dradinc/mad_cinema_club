from sqlalchemy import Column, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from src.modules.db import app_db


class RowsSeatsModel(app_db.Model):
    __tablename__ = 'rows_seats'

    # columns
    id = Column(Integer, primary_key=True)
    row = Column(Integer, nullable=False)
    position = Column(Integer, nullable=False)
    seat = Column(Integer, nullable=True)
    is_empty = Column(Boolean, nullable=False, default=False)
    # scheme relationships
    scheme_id = Column(Integer, ForeignKey('hall_scheme.id'))
    scheme = relationship('SchemeModel', back_populates='rows_seats')
    # relationships
    tickets = relationship('TicketsModel', back_populates='seat')

