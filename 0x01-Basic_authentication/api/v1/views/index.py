#!/usr/bin/env python3
""" Module of Index views
"""
from flask import jsonify, abort
import requests
from api.v1.views import app_views


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status() -> str:
    """ GET /api/v1/status
    Return:
      - the status of the API
    """
    return jsonify({"status": "OK"})


@app_views.route('/stats/', strict_slashes=False)
def stats() -> str:
    """ GET /api/v1/stats
    Return:
      - the number of each objects
    """
    from models.user import User
    stats = {}
    stats['users'] = User.count()
    return jsonify(stats)


@app_views.route('/unauthorized', methods=['GET'], strict_slashes=False)
def errorhandler() -> str:
    """ GET /api/v1/error
    Return:
      - the error message
    """
    response = jsonify({'error': 'unauthorized'})
    response.status_code = 401
    return response


@app_views.errorhandler(401)
def aun(error):

    abort(401)
