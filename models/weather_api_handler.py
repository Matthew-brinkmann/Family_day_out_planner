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
    futureUrl = "https://api.weatherapi.com/v1/future.json"
    weatherQueryUrl = ""
    params = {}

    def __init__(self, weatherRequestInformation):
        """initialise WeatherRequestHandler"""
        self.create_weather_query_params(weatherRequestInformation)

    @classmethod
    def create_weather_query_params(cls, weatherRequestInformation):
        """create weather query url"""
        if not os.environ.get('WEATHER_API_KEY'):
            raise ServerEnvironVariablesNotSet("WEATHER_API_KEY")

        selectedDayDifferences = weatherRequestInformation["selected_days_weather_api"]
        if selectedDayDifferences <= 14:
            WeatherRequestHandler.weatherQueryUrl = WeatherRequestHandler.forecastUrl
            WeatherRequestHandler.params = {
                "key": os.environ.get('WEATHER_API_KEY'),
                "q": weatherRequestInformation["place_address"],
                "days": weatherRequestInformation["selected_days_weather_api"]
            }
        elif selectedDayDifferences > 14 and selectedDayDifferences <= 300:
            WeatherRequestHandler.weatherQueryUrl = WeatherRequestHandler.futureUrl
            WeatherRequestHandler.params = {
                "key": os.environ.get('WEATHER_API_KEY'),
                "q": weatherRequestInformation["place_address"],
                "dt": weatherRequestInformation["selected_date_event_api"]
            }

    @classmethod
    def get_weather_information(cls):
        """call weather API and return weather information"""
        weatherApiResponse = requests.get(WeatherRequestHandler.weatherQueryUrl,
                                        params=WeatherRequestHandler.params,
                                        allow_redirects=False).json()
        if weatherApiResponse is None:
            raise ApiCallNonResposive
        return (WeatherRequestHandler.extract_weather_info_from_response(weatherApiResponse))

    @classmethod
    def extract_weather_info_from_response(cls, weatherApiResponse):
        """pulls out the required weather information from API call"""
        print(weatherApiResponse["forecast"]["forecastday"][-1])
        return (weatherApiResponse["forecast"]["forecastday"][-1])
