#!/usr/bin/python3
"""
module to handle all incoming requests for server side information
"""

from models.event_api_handler import EventRequestHandler
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
        eventHandler = EventRequestHandler(eventRequestInformation)
        returnEventDTO.eventList = eventHandler.get_list_of_events_from_query()
        # returnDTO.weatherInformation = get_weather_information(eventRequestInformation)
        # return (returnEventDTO.toJson())
       
        return (returnEventDTO.toJson())
