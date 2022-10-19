#!/usr/bin/python3
"""
Contains the testing module for returnDTO
"""
from models.system_logging import SystemLogging
import unittest
import os


class TestSystemLogging(unittest.TestCase):
    """
    contains unit tests for the SystemLogging.
    """
    def testLogFileCreationAndAppending(self):
        messageString = "should Be Logged"
        callerPath = "TestSystemLogging.testLogFileCreation()"
        fullErrorString = "method: " + callerPath + " raised error: " + messageString
        SystemLogging.log_warning_error(callerPath, messageString)
        self.assertEqual(True, os.path.exists("test_app.log"))
        with open('test_app.log') as myfile:
            self.assertEqual(True, fullErrorString in myfile.read())
        os.remove('test_app.log')
