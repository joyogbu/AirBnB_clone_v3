#!/usr/bin/python3
"""documenting the module"""


from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status', methods=['GET'])
def statusroute():
    """defining the function"""
    string = {
               "status": "OK"
             }
    return jsonify(string)

@app_views.route('/stats', methods=['GET'])
def retrieve_number():
    """define thw function"""
    response = {
                 "amenities": "Amenity",
                 "cities": "City",
                 "places": "Place",
                 "reviews": "Review",
                 "states": "State",
                 "users": "User"
               }
    for key, value in response.items():
        response[key] = storage.count(value)
    return jsonify(response)
