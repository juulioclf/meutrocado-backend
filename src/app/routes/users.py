from flask import Blueprint, jsonify
from app.models.user import User  

users_bp = Blueprint('users', __name__)

@users_bp.route('/users')
def login():

    users = User.query.all()

    user_list = [{'id': user.iduser, 'username': user.username} for user in users]

    return jsonify(user_list)