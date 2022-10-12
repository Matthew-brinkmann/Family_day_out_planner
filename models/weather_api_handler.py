#!usr/bin/python3
"""
module to handle all incoming request for weather information
"""

import requests
from models.exceptions import *
import os


class WeatherRequestHandler:
    """handle API for weather"""

    forecastUrl = "https://api.weatherapi.com/v1/forecast.json"
    weatherQueryUrl = ""
    params = {}
    selectedDayDifferences = 0
    weatherRequestDataVerified = True

    def __init__(self, weatherRequestInformation):
        """initialise WeatherRequestHandler"""
        self.verify_weather_request_data(weatherRequestInformation)
        self.create_weather_query_params(weatherRequestInformation)

    def create_weather_forecast_query_params(self, weatherRequestInformation):
        """create weather query url if selected is less than 14 days"""
        self.weatherQueryUrl = self.forecastUrl
        self.params = {
            "key": os.environ.get('WEATHER_API_KEY'),
            "q": weatherRequestInformation["place_address"],
            "days": weatherRequestInformation["selected_days_weather_api"]
        }

    def create_weather_query_params(self, weatherRequestInformation):
        """create weather query url"""
        if not os.environ.get('WEATHER_API_KEY'):
            raise ServerEnvironVariablesNotSet("WEATHER_API_KEY")

        if self.selectedDayDifferences <= 14:
            self.create_weather_forecast_query_params(weatherRequestInformation)

    def get_weather_information(self):
        """call weather API and return weather information"""
        if self.weatherRequestDataVerified is False:
            weatherApiResponse = {"error": "Weather forecast is only available for next 14 days."}
            return weatherApiResponse
        
        return(self.make_weather_api_call())
        
    def make_weather_api_call(self):
        """makes the weather API call"""
        weatherApiResponse = requests.get(self.weatherQueryUrl,
                                        params=self.params,
                                        allow_redirects=False).json()
        self.verify_api_response(weatherApiResponse)
        return (self.extract_weather_info_from_response(weatherApiResponse))

    @staticmethod
    def extract_weather_info_from_response(weatherApiResponse):
        """pulls out the required weather information from API call"""
        return (weatherApiResponse["forecast"]["forecastday"][-1])

    def verify_api_response(self, apiResponse):
        """tests if the response is valid"""
        if apiResponse is None:
            raise ApiCallNonResposive
        if apiResponse.get("forecast").get("forecastday") is None:
            apiResponse = {"error": "Could not retrieve weather data."}
            
    def verify_weather_request_data(self, weatherRequestInformation):
        """call weather API and return weather information"""
        if weatherRequestInformation["selected_days_weather_api"] > 14:
            self.weatherRequestDataVerified = False
        else:
            self.selectedDayDifferences = weatherRequestInformation["selected_days_weather_api"]
