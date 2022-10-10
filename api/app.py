#!/usr/bin/python3
"""module for flask app"""
from api.views import app_views
from api.views import html_views
from api.views.documentation.swagger_setup import *
import os
from flask import Flask, Blueprint, jsonify
from flask_cors import CORS
from flasgger import LazyJSONEncoder, Swagger

app = Flask(__name__, static_folder='../family-day-out/build/static', template_folder='../family-day-out/build')
app.register_blueprint(app_views)
app.register_blueprint(html_views)
# cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
corsInstance = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.json_encoder = LazyJSONEncoder
swagger = Swagger(app,
                  template=swagger_template,             
                  config=swagger_config)


@app.errorhandler(404)
def errorHandler(error):
    """returns a 404 error msg"""
    return jsonify(error='Page Not found'), 404


if __name__ == '__main__':
    app.run(host=os.getenv('FLASK_HOST') or '0.0.0.0',
            port=os.getenv('FLASK_PORT') or '5000',
            debug=os.getenv('FLASK_DEBUG') or False,
            threaded=True)