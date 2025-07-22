from flask import Blueprint, request
from controllers.user_controller import (
    get_all_users_controller,
    get_user_by_id_controller,
    create_user_controller,
    update_user_controller,
    delete_user_controller,
    search_users_controller,
    login_controller
)
from utils.validators import validate_user_input

user_routes = Blueprint('user_routes', __name__)

@user_routes.route('/users', methods=['GET'])
def get_all_users():
    return get_all_users_controller()

@user_routes.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    return get_user_by_id_controller(user_id)

@user_routes.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    errors = validate_user_input(data, ['name', 'email', 'password'])
    if errors:
        return {"errors": errors}, 400
    return create_user_controller(data)

@user_routes.route('/user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    return update_user_controller(user_id, data)

@user_routes.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    return delete_user_controller(user_id)

@user_routes.route('/search', methods=['GET'])
def search_user():
    name = request.args.get('name')
    if not name:
        return {"error": "Missing search name"}, 400
    return search_users_controller(name)

@user_routes.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    errors = validate_user_input(data, ['email', 'password'])
    if errors:
        return {"errors": errors}, 400
    return login_controller(data)
