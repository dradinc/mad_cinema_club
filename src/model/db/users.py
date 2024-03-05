from sqlalchemy import Column, String, Integer
from werkzeug.security import generate_password_hash, check_password_hash

from src.model.db import app_db


class Users(app_db.Model):
    __tablename__ = 'users'

    # columns
    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False)
    email = Column(String(64), nullable=False)
    password = Column(String(512), nullable=False)
    balance = Column(Integer, default=0)
