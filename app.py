#!/usr/bin/python3
"""module for flask app"""
from documentation.swagger_setup import *
from models.exceptions import *
from models.system_request_handler import SystemRequestHandler
import os
from flask import Flask, Blueprint, jsonify, render_template, request
from flask_cors import CORS
from flasgger import Swagger, LazyJSONEncoder
from flasgger import swag_from

app = Flask(__name__, static_folder='family-day-out/build/static', template_folder='family-day-out/build')
app.json_encoder = LazyJSONEncoder
corsInstance = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
exceptionsWithDescription = (ReturnDtoEventListNotSet, ServerEnvironVariablesNotSet)

@app.route('/')
def display_hbnb():
    """Generate page with popdown menu of states/cities"""
    return render_template('index.html')
swagger = Swagger(app, template=swagger_template,             
                  config=swagger_config)

@swag_from("documentation/event_info.yml", methods=['POST'])
@app.route('/api/event_information', methods=['POST'], strict_slashes=False)
def events():
    """ retrieves number of objects by type """
    fullReturnInformation = {}
    try:
        fullReturnInformation = SystemRequestHandler.get_all_return_information(
            request.get_json())
    except ApiCallNonResposive:
        fullReturnInformation["error"] = "API did not call"
    except exceptionsWithDescription as error:
        fullReturnInformation["error"] = str(error)

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