from sqlalchemy import Column, Integer, String

from src.modules.db import app_db


class NewsModel(app_db.Model):
    __tablename__ = 'news'

    #columns
    id = Column(Integer, primary_key=True)
    title = Column(String(32), nullable=False)
    description = Column(String(64), nullable=False)
    image = Column(String, nullable=False)

    @classmethod
    def get_news(cls):
        return cls.query.all()
