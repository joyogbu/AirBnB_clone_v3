#!/usr/bin/python3
"""documenting the module"""


from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.state import State


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
    response = {}
    objects = {
                 "Amenity": 'amenities',
                 "City": 'cities',
                 "Place": 'places',
                 "Review": 'reviews',
                 "State": 'states',
                 "User": 'users'
               }
    for key, value in objects.items():
        response[value] = storage.count(key)
    return jsonify(response)
