#!/usr/bin/python3
"""
Contains the testing module for returnDTO
"""
from models.return_data_object import ReturnDataTransferObject
import unittest


class TestReturnDTO(unittest.TestCase):
    """
    contains unit tests for the RETURN DTO
    """
    def setUp(self):
        """set up for all unittests"""
        self.testReturnObject = ReturnDataTransferObject()

    def tearDown(self):
        """tead down for tests"""
        del self.testReturnObject

    def testObjectInit(self):
        """test RDTO initialised correctly"""
        self.assertEqual(self.testReturnObject.objectInformationDictionary, {'eventList': None, 'weatherInformation': None})
        self.assertEqual(self.testReturnObject.toJson(), '{"eventList": null, "weatherInformation": null}')

    def testEventListUpdate(self):
        """test RDTO can update Event List"""
        self.assertEqual(self.testReturnObject.objectInformationDictionary, {'eventList': None, 'weatherInformation': None})
        self.assertEqual(self.testReturnObject.eventList, None)
        self.testReturnObject.eventList = 123
        self.assertEqual(self.testReturnObject.objectInformationDictionary, {'eventList': None, 'weatherInformation': None})
        self.assertEqual(self.testReturnObject.eventList, None)
        self.testReturnObject.eventList = ["test", "object"]
        self.assertEqual(self.testReturnObject.objectInformationDictionary, {'eventList': ["test", "object"], 'weatherInformation': None})
        self.assertEqual(self.testReturnObject.eventList, ["test", "object"])
        self.testReturnObject.eventList = 123
        self.assertEqual(self.testReturnObject.objectInformationDictionary, {'eventList': ["test", "object"], 'weatherInformation': None})
        self.assertEqual(self.testReturnObject.eventList, ["test", "object"])

    def testWeatherInformationUpdate(self):
        """test RDTO can update weather Information"""
        self.assertEqual(self.testReturnObject.objectInformationDictionary, {'eventList': None, 'weatherInformation': None})
        self.assertEqual(self.testReturnObject.weatherInformation, None)
        self.testReturnObject.weatherInformation = 123
        self.assertEqual(self.testReturnObject.objectInformationDictionary, {'eventList': None, 'weatherInformation': 123})
        self.assertEqual(self.testReturnObject.weatherInformation, 123)