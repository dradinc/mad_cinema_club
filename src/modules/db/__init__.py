from flask_sqlalchemy import SQLAlchemy

from src import app


app_db = SQLAlchemy(app)


# Импорт таблиц для создания
from src.model.db.users import UsersModel
from src.model.db.films import FilmsModel
from src.model.db.news import NewsModel
from src.model.db.cinema import CinemaModel
# Halls
from src.model.db.halls import HallsModel
from src.model.db.halls.scheme import SchemeModel
from src.model.db.halls.rows_seats import RowsSeatsModel

with app.app_context():
    app_db.create_all()
