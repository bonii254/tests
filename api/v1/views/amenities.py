#!/usr/bin/python3
""" objects that handles all default RestFul API actions for Amenities"""
from models.amenity import Amenity
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request


@app_views.route('/amenities', methods=["GET"], strict_slashes=False)
def all_amenities():
    """retrieves the list of all amenities"""
    amenities = storage.all(Amenity)
    if amenities is None:
        abort(404)
    amenity_list = [amenity.to_dict() for amenity in amenities.values()]
    return jsonify(amenity_list), 200


@app_views.route(
    '/amenities/<amenity_id>', methods=["GET"], strict_slashes=False)
def get_amenity(amenity_id):
    """retrieve amenity object"""
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)
    return jsonify(amenity.to_dict()), 200


@app_views.route(
    '/amenities/<amenity_id>', methods=["DELETE"], strict_slashes=False)
def delete_amenity(amenity_id):
    """delete amenity object"""
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)
    amenity.delete()
    storage.save()
    return {}, 200


@app_views.route('/amenities', methods=["POST"], strict_slashes=False)
def create_amenity():
    """create amenity object"""
    amenity_info = request.get_json()
    if amenity_info is None:
        abort(400, "Not a JSON")
    if not amenity_info.get("name"):
        abort(400, "Missing name")
    amenity = Amenity(**amenity_info)
    storage.new(amenity)
    storage.save()
    return jsonify(amenity.to_dict()), 201


@app_views.route(
    '/amenities/<amenity_id>', methods=["PUT"], strict_slashes=False)
def update_amenity(amenity_id):
    """updates amenity object"""
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)
    amenity_info = request.get_json()
    if amenity_info is None:
        abort(400, "Not a JSON")
    amenity_dict = amenity.to_dict()
    amenity_dict.update(amenity_info)
    ignore = ["__name__", "id", "created_at", "updated_at"]
    amenity_dict = {k: v for k, v in amenity_dict.items() if k not in ignore}
    for key, value in amenity_dict.items():
        setattr(amenity, key, value)
    amenity.save()
    storage.save()
    return jsonify(amenity.to_dict()), 200
