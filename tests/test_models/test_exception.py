#!/usr/bin/python3
"""
Contains the testing module for exceptions
"""
from models.exceptions import *
import unittest
import requests

class TestApiCallNonResposive(unittest.TestCase):
    """
    contains unittests for ApiCallNonResposive
    """
    def testApiCallNonResposive(self):
        """test ApiCallNonResposive exception"""
        exception = ApiCallNonResposive()
        self.assertEqual(exception.message, "API call did not return a 200 reponse")
        self.assertEqual(f"{exception}", "API call did not return a 200 reponse")

        exception_1 = ApiCallNonResposive("Test ApiCallNonResposive")
        self.assertEqual(exception_1.message, "Test ApiCallNonResposive")
        self.assertEqual(f"{exception_1}", "Test ApiCallNonResposive")

class TestReturnDtoEventListNotSet(unittest.TestCase):
    """
    contains unittests for ReturnDtoEventListNotSet
    """
    def testReturnDtoEventListNotSet(self):
        """test ReturnDtoEventListNotSet exception"""
        exception = ReturnDtoEventListNotSet()
        self.assertEqual(exception.message, "event list was sent a parameter it couldn't understand:")
        self.assertEqual(exception.typeSetTo, None)
        self.assertEqual(f"{exception}",  "event list was sent a parameter it couldn't understand: None")

        exception_1 = ReturnDtoEventListNotSet(None, "Test ReturnDtoEventListNotSet:")
        self.assertEqual(exception_1.message, "Test ReturnDtoEventListNotSet:")
        self.assertEqual(exception_1.typeSetTo, None)
        self.assertEqual(f"{exception_1}", "Test ReturnDtoEventListNotSet: None")

class TestServerEnvironVariablesNotSet(unittest.TestCase):
    """
    contains unittests for ServerEnvironVariablesNotSet
    """
    def testServerEnvironVariablesNotSet(self):
        """test ServerEnvironVariablesNotSet exception"""
        exception = ServerEnvironVariablesNotSet()
        self.assertEqual(exception.message, "Server Configuration Error: No Variable:")
        self.assertEqual(exception.typeSetTo, "")
        self.assertEqual(f"{exception}", "Server Configuration Error: No Variable: ")

        exception_1 = ServerEnvironVariablesNotSet("ENV", "Test ServerEnvironVariablesNotSet:")
        self.assertEqual(exception_1.message, "Test ServerEnvironVariablesNotSet:")
        self.assertEqual(exception_1.typeSetTo, "ENV")
        self.assertEqual(f"{exception_1}", "Test ServerEnvironVariablesNotSet: ENV")

class TestApiReturnNoneResults(unittest.TestCase):
    """
    contains unittests for ApiReturnNoneResults
    """
    def testApiReturnNoneResults(self):
        """test ApiReturnNoneResults exception"""
        exception = ApiReturnNoneResults()
        self.assertEqual(exception.message, "No events results for this query")
        self.assertEqual(f"{exception}", "No events results for this query")

        exception_1 = ApiReturnNoneResults("Test ApiReturnNoneResults")
        self.assertEqual(exception_1.message, "Test ApiReturnNoneResults")
        self.assertEqual(f"{exception_1}", "Test ApiReturnNoneResults")