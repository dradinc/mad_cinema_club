from flask_mail import Mail

from src import app


app_mail = Mail(app)
