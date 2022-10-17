#!/usr/bin/python3
"""
Contains the testing module for EventRequestHandler
"""
from models.event_api_handler import EventRequestHandler
from models.exceptions import *
import unittest
import os
from unittest.mock import MagicMock, patch
import requests


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
            "location_requested": "Melbourne VIC, Australia",
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
        self.assertRaises(ApiReturnNoneResults, self.testEventRequestHandler.verify_api_response, {"events_results": {}})

    @patch('models.event_api_handler.requests')
    def test_get_list_of_events_from_query(self, mock_requests):
        """test function get_list_of_events_from_query"""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "events_results": [
                {
                    "title": "Avi Avital",
                    "date": {
                        "start_date": "Sep 24",
                        "when": "Sat, Sep 24, 7 – 9 PM GMT+10"
                    },
                    "address": [
                        "Melbourne Recital Centre, 31 Sturt St",
                        "Southbank VIC, Australia"
                    ],
                    "link": "https://www.songkick.com/concerts/40429762-avi-avital-at-melbourne-recital-centre?utm_medium=organic&utm_source=microformat",
                    "event_location_map": {
                        "image": "https://www.google.com/maps/vt/data=2ikm3IrGV_2-ngdl3aatgFd0wRGHiRMlLfTnQSvphlNMH3xazkPtQ4KUzD4sHbI4oOtbXkhHtjTVyEEbdIJVdAUkIpLLwqoI4DzZf5gzszkeaJt8MPE",
                        "link": "https://www.google.com/maps/place//data=!4m2!3m1!1s0x6ad642ae1a5e9b83:0xef21a57877623bbe?sa=X&hl=en",
                        "serpapi_link": "https://serpapi.com/search.json?data=%214m2%213m1%211s0x6ad642ae1a5e9b83%3A0xef21a57877623bbe&engine=google_maps&google_domain=google.com&hl=en&q=Events+in+Melbourne%2C+Vic+on+24%2F09%2F2022&type=place"
                    },
                    "description": "Avi Avital and Giovanni Sollima at Melbourne Recital Centre at 2022-09-24",
                    "ticket_info": [
                        {
                            "source": "Songkick.com",
                            "link": "https://www.songkick.com/concerts/40429762-avi-avital-at-melbourne-recital-centre?utm_medium=organic&utm_source=microformat",
                            "link_type": "tickets"
                        },
                        {
                            "source": "Limelight Magazine",
                            "link": "https://limelightmagazine.com.au/event/avi-avital-giovanni-sollima-4/2022-09-24/",
                            "link_type": "more info"
                        },
                        {
                            "source": "Continuo Community",
                            "link": "https://continuo.org.au/event/avital-sollima-scarlatti-sollima-castello-frescobaldi-traditional/2022-09-24/",
                            "link_type": "more info"
                        },
                        {
                            "source": "My Community Diary",
                            "link": "https://www.mycommunitydiary.com.au/Victoria/Melbourne/Avi_Avital_and_Giovanni_Sollima/175041/3055412",
                            "link_type": "more info"
                        },
                        {
                            "source": "Common Times",
                            "link": "https://commontimes.com.au/events/avi-avital-and-giovanni-sollima-39103",
                            "link_type": "more info"
                        }
                    ],
                    "venue": {
                        "name": "Melbourne Recital Centre",
                        "rating": 4.8,
                        "reviews": 1184,
                        "link": "https://www.google.com/search?hl=en&q=Melbourne+Recital+Centre&ludocid=17231235586113813438&ibp=gwp%3B0,7"
                    },
                    "thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSu7fMd__5u6xhglIF3IEZW-E5G9ePFSCBMK90qlOkD0K4dSbSS2Sn6Ve0&s",
                    "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRyv2akIbFVKQ436gGwt-NJuojN8gmv9G8yD5sss_HzTCT6JZlxJnPrtPgrUQ&s=10"
                }
            ]
        }
        mock_requests.get.return_value = mock_response
        self.assertEqual(self.testEventRequestHandler.get_list_of_events_from_query(), [
                {
                    "title": "Avi Avital",
                    "date": {
                        "start_date": "Sep 24",
                        "when": "Sat, Sep 24, 7 – 9 PM GMT+10"
                    },
                    "address": [
                        "Melbourne Recital Centre, 31 Sturt St",
                        "Southbank VIC, Australia"
                    ],
                    "link": "https://www.songkick.com/concerts/40429762-avi-avital-at-melbourne-recital-centre?utm_medium=organic&utm_source=microformat",
                    "event_location_map": {
                        "image": "https://www.google.com/maps/vt/data=2ikm3IrGV_2-ngdl3aatgFd0wRGHiRMlLfTnQSvphlNMH3xazkPtQ4KUzD4sHbI4oOtbXkhHtjTVyEEbdIJVdAUkIpLLwqoI4DzZf5gzszkeaJt8MPE",
                        "link": "https://www.google.com/maps/place//data=!4m2!3m1!1s0x6ad642ae1a5e9b83:0xef21a57877623bbe?sa=X&hl=en",
                        "serpapi_link": "https://serpapi.com/search.json?data=%214m2%213m1%211s0x6ad642ae1a5e9b83%3A0xef21a57877623bbe&engine=google_maps&google_domain=google.com&hl=en&q=Events+in+Melbourne%2C+Vic+on+24%2F09%2F2022&type=place"
                    },
                    "description": "Avi Avital and Giovanni Sollima at Melbourne Recital Centre at 2022-09-24",
                    "ticket_info": [
                        {
                            "source": "Songkick.com",
                            "link": "https://www.songkick.com/concerts/40429762-avi-avital-at-melbourne-recital-centre?utm_medium=organic&utm_source=microformat",
                            "link_type": "tickets"
                        },
                        {
                            "source": "Limelight Magazine",
                            "link": "https://limelightmagazine.com.au/event/avi-avital-giovanni-sollima-4/2022-09-24/",
                            "link_type": "more info"
                        },
                        {
                            "source": "Continuo Community",
                            "link": "https://continuo.org.au/event/avital-sollima-scarlatti-sollima-castello-frescobaldi-traditional/2022-09-24/",
                            "link_type": "more info"
                        },
                        {
                            "source": "My Community Diary",
                            "link": "https://www.mycommunitydiary.com.au/Victoria/Melbourne/Avi_Avital_and_Giovanni_Sollima/175041/3055412",
                            "link_type": "more info"
                        },
                        {
                            "source": "Common Times",
                            "link": "https://commontimes.com.au/events/avi-avital-and-giovanni-sollima-39103",
                            "link_type": "more info"
                        }
                    ],
                    "venue": {
                        "name": "Melbourne Recital Centre",
                        "rating": 4.8,
                        "reviews": 1184,
                        "link": "https://www.google.com/search?hl=en&q=Melbourne+Recital+Centre&ludocid=17231235586113813438&ibp=gwp%3B0,7"
                    },
                    "thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSu7fMd__5u6xhglIF3IEZW-E5G9ePFSCBMK90qlOkD0K4dSbSS2Sn6Ve0&s",
                    "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRyv2akIbFVKQ436gGwt-NJuojN8gmv9G8yD5sss_HzTCT6JZlxJnPrtPgrUQ&s=10"
                }
            ]
        )
