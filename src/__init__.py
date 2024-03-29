from flask import Flask

from instance.config import Config

app = Flask(__name__)
app.config.from_object(Config)

from src.api import app_api  # Импорт модуля API
from src.modules.db import app_db  # Импорт модуля базы данных
