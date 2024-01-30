#!/usr/bin/python3
"""entry point toapi"""

from flask import Flask, jsonify
from api.v1.views import app_views
from models import storage
from os import getenv
from flask_cors import CORS

app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/*": {"origins": "0.0.0.0"}})

@app.teardown_appcontext
def teardown_appcontext(exception):
    """This function will be called when the app context is torn down."""
    storage.close()

@app.errorhandler(404)
def not_found(error):
    """handle 404 error"""
    return jsonify({"error": "Not found"})

if __name__ == "__main__":
    app.run(
        host = getenv('HBNB_API_HOST', '0.0.0.0'),
        port = int(getenv('HBNB_API_PORT', 5000)),
        threaded=True,
        debug=True,
        )
