#!/usr/bin/python3
"""documenting the module"""


from api.v1.views import app_views

@app_views.route('/status')
def statusroute():
    string = '{"status": "ok"}'
    return (string)

