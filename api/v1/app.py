#!/usr/bin/python3
"""module for flask app"""
import os
from flask import Flask, Blueprint, jsonify
from api.v1.views import app_views
from flask_cors import CORS


app = Flask(__name__)
app.register_blueprint(app_views)
corsInstance = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})


@app.errorhandler(404)
def errorHandler(error):
    """returns a 404 error msg"""
    return jsonify(error='Not found'), 404


if __name__ == '__main__':
    app.run(host=os.getenv('FLASK_HOST') or '0.0.0.0',
            port=os.getenv('FLASK_PORT') or '5000',
            threaded=True)