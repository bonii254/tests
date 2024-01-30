#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Users """

from models.user import User
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request


@app_views.route('/users', methods=["GET"], strict_slashes=False)
def all_users():
    """retrieve all users"""
    users = storage.all(User)
    if not users:
        abort(404)
    users_list = [user.to_dict() for user in users.values()]
    return jsonify(users_list), 200


@app_views.route('/users/<user_id>', methods=["GET"], strict_slashes=False)
def get_user(user_id):
    """retrieves single user object"""
    user = storage.get(User, user_id)
    if not user:
        abort(404)
    return jsonify(user.to_dict()), 200


@app_views.route('/users/<user_id>', methods=["DELETE"], strict_slashes=False)
def delete_user(user_id):
    """delete user objects"""
    user = storage.get(User, user_id)
    if not user:
        abort(404)
    user.delete()
    storage.save()
    return {}, 200


@app_views.route('/users', methods=["POST"], strict_slashes=False)
def create_user():
    """create a new user"""
    user_info = request.get_json()
    if not user_info:
        abort(400, "Not a JSON")
    if not user_info.get("email"):
        abort(400, "Missing email")
    if not user_info.get("password"):
        abort(400, "Missing password")
    user = User(**user_info)
    storage.new(user)
    storage.save()
    return jsonify(user.to_dict()), 201


@app_views.route('/users/<user_id>', methods=["PUT"], strict_slashes=False)
def update_user(user_id):
    """udates user object"""
    user = storage.get(User, user_id)
    if not user:
        abort(404)
    user_info = request.get_json()
    if not user_info:
        abort(400, "Not a JSON")
    user_dict = user.to_dict()
    user_dict.update(user_info)
    ignore = ["__name__", "id", "email", "created_at", "updated_at"]
    user_dict = {k: v for k, v in user_dict.items() if k not in ignore}
    for key, value in user_dict.items():
        setattr(user, key, value)

    user.save()
    storage.save()
    return jsonify(user.to_dict()), 200

