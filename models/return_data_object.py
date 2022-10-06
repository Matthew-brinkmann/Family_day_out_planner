#!/usr/bin/python3
"""
module to handle all incoming requests for server side information
"""
import json
from models.exceptions import *


class ReturnDataTransferObject:
    """
    contains information and serialisation for object.
    """

    def __init__(self):
        """how to initialize returnDTO"""
        self.__objectInformationDictionary = {}
        self.eventList = []
        self.weatherInformation = None

    @property
    def eventList(self):
        """
        getter for eventList
        """
        return (self.__eventList)

    @eventList.setter
    def eventList(self, eventList):
        """
        setter for eventList
        """
        if type(eventList) is list:
            self.__eventList = eventList
            self.__objectInformationDictionary["eventList"] = eventList
        else:
            raise ReturnDtoEventListNotSet(eventList)

    @property
    def weatherInformation(self):
        """
        getter for weatherInformation
        """
        return (self.__weatherInformation)

    @weatherInformation.setter
    def weatherInformation(self, weatherInformation):
        """
        setter for weatherInformation
        """
        self.__weatherInformation = weatherInformation
        self.__objectInformationDictionary["weatherInformation"] = weatherInformation

    @property
    def objectInformationDictionary(self):
        """
        getter for objectInformation Dicitonary
        """
        return (self.__objectInformationDictionary)

    def toJson(self):
        """
        turns the DTO into a JSON string.
        """
        return (json.dumps(self.objectInformationDictionary))
