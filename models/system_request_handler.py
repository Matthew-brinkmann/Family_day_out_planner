#!/usr/bin/python3
"""
module to handle all incoming requests for server side information
"""

import requests
from models.exceptions import *
from models.return_data_object import ReturnDataTransferObject


class SystemRequestHandler:
    """
    This class handles all the incoming requests via API.
    """
    @staticmethod
    def get_all_return_information(eventRequestInformation):
        """
        will call the modules to get the weather information.
        """
        # created an object to hold all the information we require here, instead of storing them in seperate variables.
        returnEventDTO = ReturnDataTransferObject()
        # returnDTO.weatherInformation = get_weather_information(eventRequestInformation)
        # return (returnEventDTO.toJson())
        url = "https://serpapi.com/search.json"
        queryUrl = "Events in "\
                   + eventRequestInformation["place_address"]\
                   + " on "\
                   + eventRequestInformation["selected_date_event_api"]
        params = {
            "engine": "google_events",
            "q": queryUrl,
            "api_key":
            "6854b791194e70560433b5c80985cc074c77e7469f89c78f7c3f82f56ac7b93a"
        }
        # below commented code has been tested, it worked. I commented it out to save our API calls
        # eventList = requests.get(url,
        #                          params=params,
        #                          allow_redirects=False
        #                          ).json()["events_results"]
        # if eventList is None:
        #     raise ApiCallNonResposive
        # returnEventDTO.eventList = eventList
        return (returnEventDTO.toJson())
