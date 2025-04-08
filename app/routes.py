# A file to define all the routes

from flask import Blueprint
from app.auth import register, login, refresh, protected

auth_bp = Blueprint('auth', __name__)

#Authentiation routes
auth_bp.route('/register', methods=['POST'])(register)
auth_bp.route('/login', methods=['POST'])(login)
auth_bp.route('/refresh', methods=['POST'])(refresh)
auth_bp.route('/protected', methods=['GET'])(protected)

