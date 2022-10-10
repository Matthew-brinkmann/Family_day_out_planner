#!/usr/bin/python3
"""Initialize Blueprint views"""
from flask import Blueprint

app_views = Blueprint("app_views", __name__, url_prefix="/api/")
html_views = Blueprint("html_views", __name__)

from api.views.index import *
from api.views.events import *
