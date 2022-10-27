from flasgger import LazyString
from flask import request

swagger_template = dict(
info = {
    'title': LazyString(lambda: 'Get Events document'),
    'version': LazyString(lambda: '0.1'),
    'description': LazyString(lambda: 'This document depicts the /api/event_information document and returns a dictionary of events and weather information.'),
    },
host = LazyString(lambda: request.host)
)
swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": 'event_information',
            "route": '/api/events',
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/apidocs/"
}