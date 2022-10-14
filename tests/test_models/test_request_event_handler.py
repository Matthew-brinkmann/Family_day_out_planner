#!/usr/bin/python3
"""
Contains the testing module for EventRequestHandler
"""
from models.event_api_handler import EventRequestHandler
from models.exceptions import *
import unittest
import os


class TestEventRequestHandler(unittest.TestCase):
    """
    contains unit tests for EventRequestHandler
    """
    def setUp(self):
        """set up for all unittests"""
        eventRequestInformation = {
            "place_address": "Melbourne VIC, Australia",
            "place_latitude": -37.8136276,
            "place_longitude": 144.9630576,
            "selected_date_event_api": "Oct 13th 2022",
            "selected_days_weather_api": 0
        }
        self.testEventRequestHandler = EventRequestHandler(eventRequestInformation)

    def tearDown(self):
        """tead down for tests"""
        del self.testEventRequestHandler

    def testObjectInit(self):
        """test RDTO initialised correctly"""
        queryUrl = "Events in Melbourne VIC, Australia on Oct 13th 2022"
        params = {
            "engine": "google_events",
            "q": queryUrl,
            "api_key": os.environ.get('EVENT_API_KEY')
        }
        url = "https://serpapi.com/search.json"
        self.assertEqual(self.testEventRequestHandler.queryUrl, queryUrl)
        self.assertEqual(self.testEventRequestHandler.params, params)
        self.assertEqual(self.testEventRequestHandler.url, url)
    
    def testExtraEventListFromResponse(self):
        """test function extract_event_list_from_response"""
        apiResponse = {
            "events_results": {
                "abc": "def"
            }
        }
        self.assertEqual(self.testEventRequestHandler.extract_event_list_from_response(apiResponse), {
            "abc": "def"
        })

    def testVerifyApiResponse(self):
        """test function verify_api_response"""
        self.assertRaises(ApiCallNonResposive, self.testEventRequestHandler.verify_api_response, None)
        self.assertRaises(ApiReturnNoneResults, self.testEventRequestHandler.verify_api_response, {})

