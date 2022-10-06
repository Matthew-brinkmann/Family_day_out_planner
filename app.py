#!/usr/bin/python3
"""module for flask app"""
from logging import exception
from models.exceptions import *
from models.system_request_handler import SystemRequestHandler
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
    fullReturnInformation = {}
    try:
        fullReturnInformation = SystemRequestHandler.get_all_return_information(
            request.get_json())
    except ApiCallNonResposive:
        fullReturnInformation["error"] = "API did not call"
    except ReturnDtoEventListNotSet as e:
        fullReturnInformation["error"] = str(e)

    return jsonify(fullReturnInformation)


@app.errorhandler(404)
def errorHandler(error):
    """returns a 404 error msg"""
    return jsonify(error='Not found'), 404


if __name__ == '__main__':
    app.run(host=os.getenv('FLASK_HOST') or '0.0.0.0',
            port=os.getenv('FLASK_PORT') or '5000',
            debug=os.getenv('FLASK_DEBUG') or False,
            threaded=True)