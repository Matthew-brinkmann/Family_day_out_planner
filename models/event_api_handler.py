#!/usr/bin/python3
"""
module to handle all incoming requests for server side information
"""

import requests
from models.exceptions import *
import os
import re


class EventRequestHandler:
    """handles API for events"""

    url = "https://serpapi.com/search.json"
    queryUrl = ""
    params = {}

    def __init__(self, eventRequestInformation):
        self.create_query_url(eventRequestInformation)
        self.create_query_params(eventRequestInformation)
        
    def get_list_of_events_from_query(self):
        """calls API and returns event List"""
        apiResponse = requests.get(self.url,
                                   params=self.params,
                                   allow_redirects=False
                                   ).json()
        self.verify_api_response(apiResponse)
        return (self.extract_event_list_from_response(apiResponse))

    def extract_event_list_from_response(self, apiResponse):
        """pulls out the correct data from the API call"""
        return (apiResponse["events_results"])

    def create_query_url(self, eventRequestInformation):
        """creates the class query URL"""
        self.queryUrl = "Events in "\
                + eventRequestInformation["place_address"]\
                + " on "\
                + eventRequestInformation["selected_date_event_api"]

    def create_query_params(self, eventRequestInformation):
        '''cerates the query parameters'''
        if not os.environ.get('EVENT_API_KEY'):
            raise ServerEnvironVariablesNotSet("EVENT_API_KEY")
        
        self.params = {
            "engine": "google_events",
            "q": self.queryUrl,
            "location_requested": eventRequestInformation["place_address"],
            "api_key": os.environ.get('EVENT_API_KEY')}

    @staticmethod
    def verify_api_response(apiResponse):
        """tests if the response is valid"""
        if apiResponse is None:
            raise ApiCallNonResposive
        if apiResponse == {}:
            raise ApiReturnNoneResults
        if apiResponse.get("events_results") is None or apiResponse.get("events_results") == {}:
            raise ApiReturnNoneResults
