#!/usr/bin/python3
"""Handles all deflault RESTFul API actions for places."""

from api.v1.views import app_views
from flask import jsonify, request, abort
from models import storage
from models.place import Place
from models.city import City


@app_views.route('/cities/<city_id>/places', methods=["GET"], strict_slashes=False)
def place_list(city_id):
    """retrieves list of places in a city"""
    city = storage.get(City, city_id)
    if not city:
        abort(404)
    places = storage.all(Place)
    return jsonify([place.to_dict() for place in places.values() if place.city_id == city_id]), 200


@app_views.route('/places/<place_id>', methods=["GET"], strict_slashes=False)
def get_object(place_id):
    """retrieve a place object"""
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    return jsonify(place.to_dict()), 200


@app_views.route('/places/<place_id>', methods=["DELETE"], strict_slashes=False)
def delete_place(place_id):
    """delete a place"""
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    place.delete()
    storage.save()
    return {}, 200


@app_views.route('/cities/<city_id>/places', methods=["POST"], strict_slashes=False)
def create_place(city_id):
    """create a place"""
    city = storage.get(City, city_id)
    if not city:
        abort(404)
    place_info = request.get_json()
    if not place_info:
        abort(400, "Not a JSON")
    if not place_info.get("user_id"):
        abort(400, "Missing user_id");
    user = storage.get(User, place_info.get("user_id"))
    if not user:
        abort(404)
    if not place_info.get("name"):
        abort(400, "Missing name")
    place = Place(**place_info)
    storage.new(place)
    storage.save()
    return jsonify(place.to_dict()), 201


@app_views.route('/places/<place_id>', methods=["PUT"], strict_slashes=False)
def update_place(place_id):
    """updates a place"""
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    place_info = request.get_json()
    if not place_info:
        abort(400, "Not a JSON")
    place_dict = place.to_dict()
    place_dict.update(place_info)
    ignore = ["__name__", "id", "user_id", "city_id", "created_at", "updated_at"]
    place_dict = {k: v for k, v in place_dict.items() if k not in ignore}
    for key, value in place_dict.items():
        setattr(place, key, value)
    place.save()
    storage.save()
    return jsonify(place.to_dict()), 200
