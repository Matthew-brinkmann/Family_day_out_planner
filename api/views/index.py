#!/usr/bin/python3
"""index.py to connect to API"""
from api.views import html_views
from flask import Flask, Blueprint, render_template, jsonify


@html_views.route('/status', strict_slashes=False)
def apiStatus():
    """API Status"""
    return jsonify({"status": "OK"})


@html_views.route('/', strict_slashes=False)
def display_hbnb():
    """Generate home page"""
    return render_template('index.html')


if __name__ == "__main__":
    pass
