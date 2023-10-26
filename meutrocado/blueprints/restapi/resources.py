from flask import jsonify, abort
from flask_restful import Resource

from meutrocado.models import User

class UserResource(Resource):
    def get(self):
        users = User.query.all() or abort (204)

        return jsonify({
            "users": [user.to_dict() for user in users]
        })
    

class UserItemResource(Resource):
    def get(self, user_id):
        user = User.query.filter_by(id=user_id).first() or abort(404)

        return jsonify(user.to_dict())