#!/usr/bin/python3
"""blueprint module"""


from flask import Blueprint
from api.v1.views.index import *


app_views = Blueprint("app_views", __name__)
