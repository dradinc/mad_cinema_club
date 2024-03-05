
class Config:
    SECRET_KEY = '3f0ab93b1fea443496882eff3b6555d5'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SQLALCHEMY_DATABASE_URI = "postgresql://<username>:<password>@<server>:5432/<db_name>"
    SQLALCHEMY_DATABASE_URI = "sqlite:///cinema_club.db"

    JSON_ADD_STATUS = False
    JWT_SECRET_KEY = 'jwt-secret-string'  # Секретный ключ для токенов

    MAIL_SERVER = 'mail.nic.ru'
    MAIL_PORT = 465
    # MAIL_USE_TLS = True
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'support@dradinc.ru'
    MAIL_DEFAULT_SENDER = 'support@dradinc.ru'
    MAIL_PASSWORD = 'Kotova8612'
