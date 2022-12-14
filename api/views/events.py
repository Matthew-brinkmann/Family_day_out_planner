#!/usr/bin/python3
"""module for flask app"""
from api.views import app_views
from api.views.documentation.swagger_setup import *
from models.exceptions import *
from models.system_request_handler import SystemRequestHandler
import os
from flask import Flask, Blueprint, jsonify, request
from flasgger import swag_from


exceptionsWithDescription = (ReturnDtoEventListNotSet, ServerEnvironVariablesNotSet)


@swag_from("documentation/event_info.yml", methods=['POST'])
@app_views.route('/events', methods=['POST'], strict_slashes=False)
def events():
    """ retrieves number of objects by type """
    fullReturnInformation = {}
    try:
        fullReturnInformation = SystemRequestHandler.get_all_return_information(
            request.get_json())
    except ApiCallNonResposive as error:
        fullReturnInformation["error"] = str(error)
    except ApiReturnNoneResults as error:
        fullReturnInformation["error1"] = str(error)
    except exceptionsWithDescription as error:
        fullReturnInformation["error2"] = str(error)

    return jsonify(fullReturnInformation)


if __name__ == "__main__":
    pass