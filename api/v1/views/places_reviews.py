#!/usr/bin/python3
"""Handles all deflault RESTFul API actions for reviews."""

from api.v1.views import app_views
from flask import jsonify, request, abort
from models import storage
from models.review import Review
from models.place import Place

@app_views.route('/places/<place_id>/reviews', methods=["GET"], strict_slashes=False)
def list_reviews(place_id):
    """retrieves a list of all reviews"""
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    reviews = storage.all(Review)
    if not reviews:
        abort(404)
    reviews_list = [review.to_dict() for review in reviews.values() if review.place_id == place_id]
    return jsonify(reviews_list), 200


@app_views.route('/reviews/<review_id>', methods=["GET"], strict_slashes=False)
def get_review(review_id):
    """retrieve a review object"""
    review = reviews.get(Review, review_id)
    if not review:
        abort(404)
    return jsonify(review.to_dict()), 200


@app_views.route('/reviews/<review_id>', methods=["DELETE"], strict_slashes=False)
def delete_review(review_id):
    """delete review object"""
    review = storage.get(Review, review_id)
    if not review:
        abort(404)
    review.delete()
    storage.save()
    return {}, 200


@app_views.route('/places/<place_id>/reviews', methods=["POST"], strict_slashes=False)
def create_review(place_id):
    """creates a new review"""
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    review_info = request.get_json()
    if not review_info:
        abort(400, "Not a JSON")
    if not review_info.get("user_id"):
        abort(400, "Missing user_id")
    user = storage.get(User, review_info.get("user_id"))
    if not user:
        abort(404)
    if not review_info.get("text"):
        abort(400, "Missing text")
    review = Review(**review_info)
    storage.new(review)
    storage.save()
    return jsonify(review.to_dict()), 201


@app_views.route('/reviews/<review_id>', methods=["PUT"], strict_slashes=False)
def update_review(review_id):
    """updates a review object"""
    review = storage.get(Review, review_id)
    if not review:
        abort(404)
    review_info = request.get_json()
    if not review_info:
        abort(400, "Not a JSON")
    review_dict = review.to_dict()
    review_dict.update(review_info)
    ignore = ["__name__", "id", "user_id", "place_id", "created_at", "updated_at"]
    review_dict = {k: v for k, v in review_dict.items() if k not in ignore}
    for key, value in review_dict.items():
        setattr(review, key, value)

    review.save()
    storage.save()
    return jsonify(review.to_dict()), 200
