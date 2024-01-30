#!/usr/bin/python3
"""a new view for State objects that handles all default RESTFul API actions"""
from flask import jsonify, request, abort
from api.v1.views import app_views
from models.state import State
from werkzeug.exceptions import NotFound
from models import storage


@app_views.route('/states',  methods=["GET"], strict_slashes=False)
def states():
    """Retrieves the list of all State objects"""
    try:
        states = storage.all("State")
        json_states = jsonify([state.to_dict() for state in states.values()])
        return json_states, 200
    except Exception as e:
        return str(e), 500


@app_views.route('/states/<string:state_id>',
                 methods=["GET"], strict_slashes=False)
def states_id(state_id):
    """retrieves state object linked to the id"""
    try:
        state = storage.get("State", state_id)
        if state is None:
            abort(404)
        json_state = jsonify(state.to_dict())
        return json_state, 200
    except Exception as e:
        return str(e), 500


@app_views.route('/states/<string:state_id>',
                 methods=["DELETE"], strict_slashes=False)
def delete(state_id):
    """deletes a state object"""
    try:
        state = storage.get(State, state_id)
        if state is None:
            abort(404)
        state.delete()
        storage.save()
        return {}, 200
    except Exception as e:
        return str(e), 500


@app_views.route('/states',  methods=["POST"], strict_slashes=False)
def post():
    """creates a state"""
    try:
        state_info = request.get_json()
        if not state_info:
            abort(400, "Not a json")
        if not state_info.get('name'):
            abort(400, 'Missing, name')
        state = State(**state_info)
        storage.new(state)
        storage.save()
        return jsonify(state.to_dict()), 201
    except Exception as e:
        return str(e), 500


@app_views.route('/states/<string:state_id>',
                 methods=["PUT"], strict_slashes=False)
def update(state_id):
    """updates state object"""
    try:
        state = storage.get(State, state_id)
        if state is None:
            abort(404)
        state_info = request.get_json()
        if not state_info:
            abort(400, "Not a JSON")
        state_dict = state.to_dict()
        state_dict.update(state_info)
        ignore = ['id', 'created_at', 'updated_at']
        state_dict = {k: v for k, v in state_dict.items() if k not in ignore}
        for key, value in state_dict.items():
            setattr(state, key, value)
        state.save()
        storage.save()
        return jsonify(state.to_dict()), 200
    except NotFound as e:
        return str(e), 404
    except Exception as e:
        return str(e), 500
