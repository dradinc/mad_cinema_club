from datetime import datetime

from flask_restful import Resource
from flask_json import json_response
from flask_jwt_extended import jwt_required, current_user

from src.model.db.tickets import TicketsModel


class CheckTicket(Resource):

    @jwt_required()
    def post(self, cinema_id: int, ticket_number: str):
        # Пользователь имеет права на проверку билетов
        if not current_user.is_checker:
            return json_response(
                status_=403,
                message='У Вас нет прав'
            )
        # Текущий билет
        current_ticket = TicketsModel.get_ticket_use_number(ticket_number)
        # Проверяем, что билет из кинотеатра в котором проводится проверка
        if not current_ticket.session.hall.cinema_id == cinema_id:
            return json_response(
                status_=406,
                message='Данный билет предназначен для другого кинотеатра'
            )
        # Проверяем, что билет сегодняшней даты
        if not current_ticket.session.date == datetime.now().date():
            return json_response(
                status_=406,
                message='Билет назначен на другую дату'
            )
        # Проверяем, что время сеанса попадает в диапазон
        if datetime.now().time() > current_ticket.session.time:
            is_start_session = True
            time1 = datetime.combine(datetime.min, datetime.now().time())
            time2 = datetime.combine(datetime.min, current_ticket.session.time)
        else:
            is_start_session = False
            time2 = datetime.combine(datetime.min, datetime.now().time())
            time1 = datetime.combine(datetime.min, current_ticket.session.time)
        time_difference = (time1 - time2).seconds / 60
        if is_start_session and time_difference > 5:
            return json_response(
                status_=406,
                messsage='Регистрация на сеанс возможна не позднее чем через 5 минут после начала'
            )
        elif not is_start_session and time_difference > 10:
            return json_response(
                status_=406,
                message='Регистрация на сеанс возможно не ранее чем за 10 минут до начала сеанса'
            )
        else:
            # Проверяем что текущий билет не был использован ранее
            app.logger.info(current_ticket.is_check)
            if current_ticket.is_check:
                return json_response(
                    status_=406,
                    message='Данный билет уже был использован'
                )
            # Далее необходимо получить все билеты пользователя на этот сеанс
            user_session_tickets = current_ticket.get_all_user_ticket_for_session()
            ticket_info = {
                'time': current_ticket.session.time.strftime('%H:%M'),
                'hall': current_ticket.session.hall.title,
                'seat_list': []
            }
            for ticket in user_session_tickets:
                ticket.check_ticket()
                ticket_info['seat_list'].append({
                    'row': ticket.seat.row,
                    'seat': ticket.seat.seat
                })
            return json_response(
                status_=200,
                ticket_info=ticket_info
            )
