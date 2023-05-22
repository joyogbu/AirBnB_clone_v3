#!/usr/bin/python3
"""testing the Api"""


from api.v1.views import app_views
from flask import Flask
from models import storage
import os


app = Flask(__name__)

host = os.getenv('HBNB_API_HOST', '0.0.0.0')
port = os.getenv('HBNB_API_PORT', 5000)

app.register_blueprint(app_views)


@app.teardown_appcontext
def close(exc):
    """defining the function"""
    storage.close()


if __name__ == "__main__":
    """run flask app"""
    app.run(host=host, port=port, threaded=True)
