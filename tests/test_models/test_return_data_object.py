#!/usr/bin/python3
"""
Contains the testing module for returnDTO
"""
from models.return_data_object import ReturnDataTransferObject
from models.exceptions import *
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
        self.assertEqual(self.testReturnObject.objectInformationDictionary, {'eventList': [], 'weatherInformation': None})
        self.assertEqual(self.testReturnObject.toJson(), '{"eventList": [], "weatherInformation": null}')

    def testEventListUpdate(self):
        """test RDTO can update Event List"""
        self.assertEqual(self.testReturnObject.objectInformationDictionary, {'eventList': [], 'weatherInformation': None})
        self.assertEqual(self.testReturnObject.eventList, [])
        self.testReturnObject.eventList = ["test", "object"]
        self.assertEqual(self.testReturnObject.objectInformationDictionary, {'eventList': ["test", "object"], 'weatherInformation': None})
        self.assertEqual(self.testReturnObject.eventList, ["test", "object"])

    def testExceptionRaise(self):
        with self.assertRaises(ReturnDtoEventListNotSet):
            self.testReturnObject.eventList = 123
        with self.assertRaises(ReturnDtoEventListNotSet):
            self.testReturnObject.eventList = None
            

    def testWeatherInformationUpdate(self):
        """test RDTO can update weather Information"""
        self.assertEqual(self.testReturnObject.objectInformationDictionary, {'eventList': [], 'weatherInformation': None})
        self.assertEqual(self.testReturnObject.weatherInformation, None)
        self.testReturnObject.weatherInformation = 123
        self.assertEqual(self.testReturnObject.objectInformationDictionary, {'eventList': [], 'weatherInformation': 123})
        self.assertEqual(self.testReturnObject.weatherInformation, 123)