#!/usr/bin/python3
""" view for City objects that handles all default RESTFul API actions"""

from api.v1.views import app_views
from flask import jsonify, request, abort
from models import storage
from models.city import City
from models.state import State
from werkzeug.exceptions import NotFound


@app_views.route(
    '/states/<state_id>/cities', methods=["GET"], strict_slashes=False)
def allcities(state_id):
    """retrieves all cities in a state"""
    try:
        state = storage.get(State, state_id)
        if not state:
            abort(404)
        cities = storage.all(City)
        json_cities = jsonify(
            [city.to_dict() for city in cities.values()
                if city.state_id == state_id])

        return json_cities, 200
    except Exception as e:
        return str(e), 500


@app_views.route('/cities/<city_id>', methods=["GET"], strict_slashes=False)
def get_city(city_id):
    """retrieves City object"""
    try:
        city = storage.get(City, city_id)
        if city is None:
            abort(404)
        return jsonify(city.to_dict()), 200
    except Exception as e:
        return str(e), 500


@app_views.route('/cities/<city_id>', methods=["DELETE"], strict_slashes=False)
def delete_city(city_id):
    """delete a city object"""
    try:
        city = storage.get(City, city_id)
        if city is None:
            abort(404)
        city.delete()
        storage.save()
        return {}, 200
    except Exception as e:
        return str(e), 500


@app_views.route(
    '/states/<state_id>/cities', methods=["POST"], strict_slashes=False)
def post_city(state_id):
    """creates a city"""
    try:
        state = storage.get(State, state_id)
        if not state:
            abort(404)
        city_info = request.get_json()
        if city_info is None:
            abort(400, "Not a JSON")
        if not city_info.get("name"):
            abort(400, "Missing name")
        city_info["state_id"] = state_id
        city = City(**city_info)
        storage.new(city)
        storage.save()
        return jsonify(city.to_dict()), 201
    except Exception as e:
        return str(e), 500


@app_views.route('/cities/<city_id>', methods=["PUT"], strict_slashes=False)
def update_city(city_id):
    """updates city object"""
    try:
        city = storage.get(City, city_id)
        if city is None:
            abort(404)
        city_info = request.get_json()
        if city_info is None:
            abort(400, "Not a JSON")
        city_dict = city.to_dict()
        city_dict.update(city_info)
        ignore = ["__class__", "id", "state_id", "created_at", "updated_at"]
        city_dict = {k: v for k, v in city_dict.items() if k not in ignore}
        for key, value in city_dict.items():
            setattr(city, key, value)

        city.save()
        return jsonify(city.to_dict()), 200
    except Exception as e:
        return str(e), 500
