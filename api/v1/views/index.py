#!/usr/bin/python3
"""documenting the module"""


from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'])
def statusroute():
    """defining the function"""
    string = {
               "status": "ok"
             }
    return jsonify(string)

