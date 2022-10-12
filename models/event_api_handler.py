#!/usr/bin/python3
"""
module to handle all incoming requests for server side information
"""

import requests
from models.exceptions import *
import os


class EventRequestHandler:
    """handles API for events"""

    url = "https://serpapi.com/search.json"
    queryUrl = ""
    params = {}

    def __init__(self, eventRequestInformation):
        self.create_query_url(eventRequestInformation)
        self.create_query_params()
        
    @classmethod
    def get_list_of_events_from_query(cls):
        """calls API and returns event List"""
        apiResponse = requests.get(EventRequestHandler.url,
                                   params=EventRequestHandler.params,
                                   allow_redirects=False
                                   ).json()
        cls.verify_api_response(apiResponse)
        return (EventRequestHandler.extract_event_list_from_response(apiResponse))

    @classmethod
    def extract_event_list_from_response(cls, apiResponse):
        """pulls out the correct data from the API call"""
        return (apiResponse["events_results"])

    @classmethod
    def create_query_url(cls, eventRequestInformation):
        """creates the class query URL"""
        EventRequestHandler.queryUrl = "Events in "\
                + eventRequestInformation["place_address"]\
                + " on "\
                + eventRequestInformation["selected_date_event_api"]

    @classmethod
    def create_query_params(cls):
        '''cerates the query parameters'''
        if not os.environ.get('EVENT_API_KEY'):
            raise ServerEnvironVariablesNotSet("EVENT_API_KEY")
        
        EventRequestHandler.params = {
            "engine": "google_events",
            "q": EventRequestHandler.queryUrl,
            "api_key": os.environ.get('EVENT_API_KEY')}

    @classmethod
    def verify_api_response(cls, apiResponse):
        """tests if the response is valid"""
        if apiResponse is None:
            raise ApiCallNonResposive
        if apiResponse.get("events_results") is None:
            print("\n\n\tin this exception\n\n")
            raise ApiReturnNoneResults
