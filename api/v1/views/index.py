#!/usr/bin/python3
"""route that print ok ok"""
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status', strict_slashes=False)
def status():
    return jsonify({"status": "OK"}), 200

@app_views.route('/stats', strict_slashes=False)
def stats():
    """endpoint that retrieves the number of each objects by type"""
    counts = {
        "Amenity": "amenities",
        "City": "cities",
        "Place": "places",
        "Review": "reviews",
        "State": "states",
        "User": "users",
    }
    values = {}
    for key, value in counts.items():
        values[value] = storage.count(key)
    return jsonify(values)
