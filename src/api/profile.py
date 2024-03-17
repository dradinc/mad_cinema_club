from flask_restful import Resource
from flask_json import json_response
from flask_jwt_extended import current_user, jwt_required


class Profile(Resource):

    @jwt_required()
    def get(self):
        return json_response(
            status_=200,
            user_info={
                "name": current_user.name,
                "email": current_user.email,
                "balance": current_user.balance
            }
        )
