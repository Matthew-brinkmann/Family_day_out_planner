#!/usr/bin/python3
"""Flask app to generate complete html page containing location/amenity
dropdown menus and rental listings"""
from flask import Flask, render_template
app = Flask('web_dynamic')
app.url_map.strict_slashes = False


@app.route('/index')
def display_hbnb():
    """Generate page with popdown menu of states/cities"""
    return render_template('testFE_local.html')