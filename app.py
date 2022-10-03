#!/usr/bin/python3
"""module for flask app"""
from distutils.log import debug
import os
from flask import Flask, Blueprint, jsonify, render_template, request
from flask_cors import CORS


app = Flask(__name__)
corsInstance = CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/')
def display_hbnb():
    """Generate page with popdown menu of states/cities"""
    return render_template('index.html')


@app.route('/status', strict_slashes=False)
def jsonStatus():
    """ returns a JSON: "status": "OK" """
    return jsonify(status='OK')


@app.route('/stats', methods=['GET'], strict_slashes=False)
def stats():
    """ retrieves number of objects by type """
    
    return jsonify(stats='None')


@app.route('/events', methods=['POST'], strict_slashes=False)
def events():
    """ retrieves number of objects by type """
    info = request.get_json()
    info["found"] = "we got here"
    return jsonify(info)


@app.errorhandler(404)
def errorHandler(error):
    """returns a 404 error msg"""
    return jsonify(error='Not found'), 404


if __name__ == '__main__':
    app.run(host=os.getenv('FLASK_HOST') or '0.0.0.0',
            port=os.getenv('FLASK_PORT') or '5000',
            debug=os.getenv('FLASK_DEBUG') or False,
            threaded=True)