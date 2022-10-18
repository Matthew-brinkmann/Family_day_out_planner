#!/usr/bin/python3
"""
Contains the testing module for WeatherRequestHandler
"""
from models.weather_api_handler import WeatherRequestHandler
from models.exceptions import *
import unittest
from unittest.mock import MagicMock, patch
import os
import requests


class TestWeatherRequestHandler(unittest.TestCase):
    """
    contains unit tests for WeatherRequestHandler
    """
    def setUp(self):
        """set up for all unittests"""
        weatherRequestInformation = {
            "place_address": "Melbourne VIC, Australia",
            "selected_days_weather_api": 0
        }
        self.testWeatherRequestHandler = WeatherRequestHandler(weatherRequestInformation)

        weatherRequestInformation_1 = {
            "place_address": "Melbourne VIC, Australia",
            "selected_days_weather_api": 15
        }
        self.testWeatherRequestHandler_1 = WeatherRequestHandler(weatherRequestInformation_1)
 
    def tearDown(self):
        """tead down for tests"""
        del self.testWeatherRequestHandler

    def testObjectInit(self):
        """test WeatherRequestHandler initialised correctly"""
        params = {
            "key": os.environ.get('WEATHER_API_KEY'),
            "q": "Melbourne VIC, Australia",
            "days": 0
        }

        forecastUrl = "https://api.weatherapi.com/v1/forecast.json"
        self.assertEqual(self.testWeatherRequestHandler.weatherQueryUrl, forecastUrl)
        self.assertEqual(self.testWeatherRequestHandler.params, params)
        self.assertEqual(self.testWeatherRequestHandler.selectedDayDifferences, 0)
        self.assertEqual(self.testWeatherRequestHandler.weatherRequestDataVerified, True)
        self.assertEqual(self.testWeatherRequestHandler_1.weatherRequestDataVerified, False)
        self.assertEqual(self.testWeatherRequestHandler_1.weatherQueryUrl, "")
        self.assertEqual(self.testWeatherRequestHandler_1.params, {})

    def test_extract_weather_info_from_response(self):
        """test function extract_weather_info_from_response"""
        weatherApiResponse = {
            "forecast": {
                "forecastday": [{"day": {"sss": "xxx"}}, {"day": {"qqq": "eee"}}]
            }
        }
        self.assertEqual(self.testWeatherRequestHandler.extract_weather_info_from_response(weatherApiResponse), {"qqq": "eee"})

    def test_get_weather_information(self):
        """test function get_weather_information"""
        weatherApiResponse = {"error": "Weather forecast is only available for next 14 days."}
        self.assertEqual(self.testWeatherRequestHandler_1.get_weather_information(), weatherApiResponse)

    def test_verify_api_response(self):
        """test function verify_api_response"""
        self.assertRaises(ApiCallNonResposive, self.testWeatherRequestHandler.verify_api_response, None)
        self.assertRaises(ApiReturnNoneResults, self.testWeatherRequestHandler.verify_api_response, {})
        self.assertRaises(ApiReturnNoneResults, self.testWeatherRequestHandler.verify_api_response, {"forecast": {}})
        self.assertRaises(ApiReturnNoneResults, self.testWeatherRequestHandler.verify_api_response, {"forecast": {"forecastday": []}})
        self.assertRaises(ApiReturnNoneResults, self.testWeatherRequestHandler.verify_api_response, {"forecast": {"forecastday": {}}})
        self.assertRaises(ApiReturnNoneResults, self.testWeatherRequestHandler.verify_api_response, {"forecast": {"forecastday": [{"abc": "def"}]}})
        self.assertRaises(ApiReturnNoneResults, self.testWeatherRequestHandler.verify_api_response, {"forecast": {"forecastday": [{"day": {}}]}})

    def run_verify_api_response_correct(self):
        """test if verify ok"""
        try:
            self.testWeatherRequestHandler.verify_api_response({"forecast": {"forecastday": [{"day": {"123": "123"}}]}})
        except ApiReturnNoneResults:
            self.fail("weather verify response raise an exeception!")

    @patch('models.weather_api_handler.requests')
    def test_make_weather_api_call(self, mock_requests):
        """test function make_weather_api_call"""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "forecast": {
                "forecastday": [
                    {
                        "day": {
                            "maxtemp_c": 11.8,
                            "maxtemp_f": 53.2,
                            "mintemp_c": 10.8,
                            "mintemp_f": 51.4,
                            "avgtemp_c": 11.5,
                            "avgtemp_f": 52.6,
                            "maxwind_mph": 2.5,
                            "maxwind_kph": 4.0,
                            "totalprecip_mm": 21.3,
                            "totalprecip_in": 0.84,
                            "avgvis_km": 7.4,
                            "avgvis_miles": 4.0,
                            "avghumidity": 88.0,
                            "daily_will_it_rain": 1,
                            "daily_chance_of_rain": 87,
                            "daily_will_it_snow": 0,
                            "daily_chance_of_snow": 0,
                            "condition": {
                                "text": "Heavy rain",
                                "icon": "//cdn.weatherapi.com/weather/64x64/day/308.png",
                                "code": 1195
                            },
                            "uv": 3.0
                        }
                    }
                ]
            }
        }
        mock_requests.get.return_value = mock_response
        self.assertEqual(self.testWeatherRequestHandler.make_weather_api_call(), {
                        "maxtemp_c": 11.8,
                        "maxtemp_f": 53.2,
                        "mintemp_c": 10.8,
                        "mintemp_f": 51.4,
                        "avgtemp_c": 11.5,
                        "avgtemp_f": 52.6,
                        "maxwind_mph": 2.5,
                        "maxwind_kph": 4.0,
                        "totalprecip_mm": 21.3,
                        "totalprecip_in": 0.84,
                        "avgvis_km": 7.4,
                        "avgvis_miles": 4.0,
                        "avghumidity": 88.0,
                        "daily_will_it_rain": 1,
                        "daily_chance_of_rain": 87,
                        "daily_will_it_snow": 0,
                        "daily_chance_of_snow": 0,
                        "condition": {
                            "text": "Heavy rain",
                            "icon": "//cdn.weatherapi.com/weather/64x64/day/308.png",
                            "code": 1195
                        },
                        "uv": 3.0
                    })

