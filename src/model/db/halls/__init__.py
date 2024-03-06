from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from src.modules.db import app_db


class HallsModel(app_db.Model):
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
