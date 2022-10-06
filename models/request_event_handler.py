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
        # below commented code has been tested, it worked. I commented it out to save our API calls
        apiResponse = requests.get(EventRequestHandler.url,
                                 params=EventRequestHandler.params,
                                 allow_redirects=False
                                 ).json()
        if apiResponse is None:
            raise ApiCallNonResposive
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
        EventRequestHandler.params = {
            "engine": "google_events",
            "q": EventRequestHandler.queryUrl,
            "api_key":os.environ['EVENT_API_KEY']}
