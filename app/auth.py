from flask import jsonify, request
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity
from app.users import UserStore

def register():
    data = request.get_json()

    # Check if data, username or password is null
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({"message" : "Missing username or password"}), 400 # Bad request

    # Check if user already exists
    if UserStore.get_user(data['username']):
        return jsonify({"message" : "User already exists"}), 400 # Bad request

    # Create User
    UserStore.create_user(data['username'], data['password'])
    return jsonify({"message" : "User created successfully"}), 201 # Created

def login():
    data = request.get_json()

    # Check if data is present
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({"message" : "Missing username or password"}), 400 # Bad Request

    # Check whether the credentials are valid
    if not UserStore.verify_user(data['username'], data['password']):
        return jsonify({"message" : "Username or password is incorrect"}), 401 # Unauthorized

    user = UserStore.get_user(data['username'])
    access_token = create_access_token(identity=user['id'])
    refresh_token = create_refresh_token(identity=user['id'])

    return jsonify({
        "access_token" : access_token,
        "refresh_token" : refresh_token
    }), 200 #Ok


@jwt_required(refresh=True)
def refresh():
    current_user = get_jwt_identity()
    new_token = create_access_token(identity=current_user)
    return jsonify({"access_token" : new_token}), 200 # OK

@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200
