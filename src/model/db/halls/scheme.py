from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from src.modules.db import app_db


class SchemeModel(app_db.Model):
    """
    Сама по себе незамысловатая таблица, предназначенная хранить схемы залов.
    В связке с таблицами Залы (halls) и Ряды и Места (rows_seats) образует схему зала.
    Также предполагается, что одни и те же схемы залов могут использоваться повторно,
    как в одном, так и в разных кинотеатрах.\n
    < id > - идентификатор схемы\n
    < title > - наименование схемы
    """
    __tablename__ = 'hall_scheme'

    # column
    id = Column(Integer, primary_key=True)
    title = Column(String(16), nullable=True)
    # relationships
    halls = relationship('HallsModel', back_populates='scheme')
    rows_seats = relationship('RowsSeatsModel', back_populates='scheme')
