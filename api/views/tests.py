#!/usr/bin/python3
"""module for flask app"""
from api.views import app_views
from api.views.documentation.swagger_setup import *
import json
from flask import abort, Flask, Blueprint, jsonify, request
from flasgger import swag_from
from tests.test_data.test_api_return import *
from models.authorization_handler import AuthorizationHandler


@swag_from("documentation/test_event_info.yml", methods=['POST'])
@app_views.route('test/event_information', methods=['POST'], strict_slashes=False)
def test_events():
    """ returns the test information """
    AuthorizationHandler.add_to_user_search_history(request)
    try:
        TestingEventApi.verify_request_is_correct(request.get_json())
    except TestRequestDataIncorrectFormat:
        abort(400, description="Data sent was not correct format")
    return(jsonify(json.dumps(test_return_dto)))