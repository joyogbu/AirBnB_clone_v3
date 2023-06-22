#!/usr/bin/python3
"""testing the Api"""


from api.v1.views import app_views
from flask import Flask, jsonify, make_response
from models import storage
import os
from flask_cors import CORS


app = Flask(__name__)
CORS(app, origins="0.0.0.0/")
host = os.getenv('HBNB_API_HOST', '0.0.0.0')
port = os.getenv('HBNB_API_PORT', 5000)
app.register_blueprint(app_views)
CORS(app_views)

@app.teardown_appcontext
def close(exc):
    """defining the function"""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """define the function"""
    return make_response(jsonify({"error": 'Not found'}), 404)


if __name__ == "__main__":
    """run flask app"""
    app.run(host=host, port=port, threaded=True)
