from flask_sqlalchemy import SQLAlchemy

from src import app


app_db = SQLAlchemy(app)


# Импорт таблиц для создания
from src.model.db.users import UsersModel

with app.app_context():
    app_db.create_all()
