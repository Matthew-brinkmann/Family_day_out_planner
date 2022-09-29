#!/usr/bin/python3
"""
flask application module
"""

from api.v1.views import app_views
from flask import Flask, jsonify


@app_views.route('/status', strict_slashes=False)
def jsonStatus():
    """ returns a JSON: "status": "OK" """
    return jsonify(status='OK')


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def stats():
    """ retrieves number of objects by type """
    
    return jsonify(stats='None')