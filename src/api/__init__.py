from flask_restful import Api

from src import app
from src.modules.jwt import app_jwt

app_api = Api(app)

# Resource import
from src.api.test_request import TestRequest, TestJwtRequest

# Auth user
from src.api.auth.sign_up import SignUp
from src.api.auth.sign_in import SignIn
from src.api.auth.forgot_password import SendCode, CheckCode, ResetPassword
# Films
from src.api.films.main_screen import MainScreenFilms
from src.api.films.current_film import CurrentFilm
from src.api.films.sessions import FilmSessions
# Cinema
from src.api.cinema.cinema_screen import CinemaScreen
from src.api.cinema.sessions import CinemaSessions
# News
from src.api.news import News
# Session
from src.api.session.session_hall import SessionHall
# Tickets
from src.api.tickets import Tickets


# api endpoint
app_api.add_resource(TestRequest, '/api/test')
app_api.add_resource(TestJwtRequest, '/api/test-jwt')
# Auth user
app_api.add_resource(SignUp, '/api/sign-up')
app_api.add_resource(SignIn, '/api/sign-in')
app_api.add_resource(SendCode, '/api/forgot-password/send-code')
app_api.add_resource(CheckCode, '/api/forgot-password/check-code')
app_api.add_resource(ResetPassword, '/api/forgot-password/reset-password')
# Films
app_api.add_resource(MainScreenFilms, '/api/films/main-screen')
app_api.add_resource(CurrentFilm, '/api/films/<film_id>')
app_api.add_resource(FilmSessions, '/api/films/<film_id>/sessions')
# Cinema
app_api.add_resource(CinemaScreen, '/api/cinema')
app_api.add_resource(CinemaSessions, '/api/cinema/<cinema_id>/sessions')
# News
app_api.add_resource(News, '/api/news')
# Session
app_api.add_resource(SessionHall, '/api/session/<int:session_id>')
# Tickets
app_api.add_resource(Tickets, '/api/tickets')
