#!/usr/bin/python3
"""module for flask app"""
from api.views import app_views
from api.views.documentation.swagger_setup import *
import json
from flask import abort, Flask, Blueprint, jsonify, request
from flasgger import swag_from
from tests.test_data.test_api_return import *


@swag_from("documentation/test_event_info.yml", methods=['POST'])
@app_views.route('test/events', methods=['POST'], strict_slashes=False)
def test_events():
    """ returns the test information """
    try:
        TestingEventApi.verify_request_is_correct(request.get_json())
    except TestRequestDataIncorrectFormat:
        abort(400, description="Data sent was not correct format")
    return(jsonify(json.dumps(test_return_dto)))

@swag_from("documentation/login_success.yml", methods=['POST'])
@app_views.route('test/login_success', methods=['POST'], strict_slashes=False)
def test_login_success():
    """ returns the test information """
    request_data=request.get_json()
    test_return_dto = {
        "username": request_data["username"],
        "password": request_data["password"],
        "message": "login successful",
        "token": "unique-token"
    }
    return(jsonify(json.dumps(test_return_dto)))

@swag_from("documentation/login_fail.yml", methods=['POST'])
@app_views.route('test/login_fail', methods=['POST'], strict_slashes=False)
def test_login_fail():
    """ returns the test information """
    test_return_dto = {
        "message": "user/password not correct, please check details and try again"
    }
    return(jsonify(json.dumps(test_return_dto)))