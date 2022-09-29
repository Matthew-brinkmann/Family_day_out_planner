#!/usr/bin/python3
"""Flask app to generate complete html page containing location/amenity
dropdown menus and rental listings"""
import os
from flask import Flask, render_template
app = Flask('web_dynamic')
app.url_map.strict_slashes = False


@app.route('/index')
def display_hbnb():
    """Generate page with popdown menu of states/cities"""
    return render_template('testFE_local.html')


if __name__ == '__main__':
    app.run(host=os.getenv('FLASK_HOST') or '0.0.0.0',
            port=os.getenv('FLASK_PORT') or '5000',
            threaded=True)