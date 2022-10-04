#!/usr/bin/python3
"""
module to handle all incoming requests for server side information
"""

from models.exceptions import *
from models.return_data_object import ReturnDataTransferObject

class system_request_handler:
    """
    This class handles all the incoming requests via API.
    """
    def get_event_information(self, eventRequestInformation):
        """
        will call the modules to get the weather information.
        """
        # created an object to hold all the information we require here, instead of storing them in seperate variables.
        returnDTO = ReturnDataTransferObject()
        # the following code will become uncommented as we bring the backend together.
        # returnDTO.eventList = get_event_information(eventRequestInformation)
        # returnDTO.weatherInformation = get_weather_information(eventRequestInformation)
        return (returnDTO.toJson())