from sqlalchemy import Column, Integer, Double, String
from sqlalchemy.orm import relationship

from src.modules.db import app_db


class CinemaModel(app_db.Model):
    __tablename__ = 'cinema'

    #column
    id = Column(Integer, primary_key=True)
    title = Column(String(32), nullable=False)
    latitude = Column(Double, nullable=False)
    longitude = Column(Double, nullable=False)
    # relationships
    halls = relationship('HallsModel', back_populates='cinema')

    @classmethod
    def get_all_cinema(cls):
        return cls.query.all()