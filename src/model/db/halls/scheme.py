from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from src.modules.db import app_db


class SchemeModel(app_db.Model):
    __tablename__ = 'hall_scheme'

    # column
    id = Column(Integer, primary_key=True)
    title = Column(String(16), nullable=True)
    # relationships
    halls = relationship('HallsModel', back_populates='scheme')
    rows_seats = relationship('RowsSeatsModel', back_populates='scheme')
