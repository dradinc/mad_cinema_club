from flask_sqlalchemy import SQLAlchemy

from src import app


app_db = SQLAlchemy(app)


# Импорт таблиц для создания
from src.model.db.users import UsersModel
from src.model.db.films import FilmsModel
from src.model.db.news import NewsModel

with app.app_context():
    app_db.create_all()
