from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash

from src.modules.db import app_db
from src.modules.jwt import app_jwt


class UsersModel(app_db.Model):
    """
    Таблица предназначенная для хранения информации о пользователях.\n
    < id > - идентификатор пользователя\n
    < name > - имя пользователя\n
    < email > - почта пользователя для верификации\n
    < password > - пароль пользователя\n
    < balance > - баланс баллов пользователя\n
    < code > - поле для хранения кода верификации пользователя\n
    """
    __tablename__ = 'users'

    # columns
    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=True)
    email = Column(String(64), nullable=False)
    password = Column(String(512), nullable=True)
    balance = Column(Integer, nullable=False, default=0)
    code = Column(String(6))
    is_checker = Column(Boolean, nullable=False, default=False)
    # relationships
    tickets = relationship('TicketsModel', back_populates='user')

    def __init__(self, new_email):
        self.email = new_email

    def add_new_user(self):
        """
        Метод добавляющий нового пользователя в систему
        :return:
        """
        app_db.session.add(self)
        app_db.session.commit()

    def edit_user(self, **kwargs):
        """
        Метод обновляющий данные пользователя (кроме id)
        :param kwargs:
        :return:
        """
        for key, value in kwargs.items():
            if key == 'id':
                continue
            elif key == 'password':
                setattr(self, key, generate_password_hash(value))
                continue
            setattr(self, key, value)
        app_db.session.commit()

    def check_password(self, password):
        return check_password_hash(self.password, password)

    @classmethod
    def find_user_by_email(cls, email):
        return cls.query.filter_by(email=email).first()


@app_jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data['sub']
    return UsersModel.query.filter(UsersModel.id == identity).one_or_none()
