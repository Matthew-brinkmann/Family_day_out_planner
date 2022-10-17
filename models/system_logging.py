import logging
import os
import string
from models.exceptions import *
from models.slack_handler import SlackChannelHandler


class SystemLogging:
    """handles the system logging"""
    if os.getenv('RUN_UNITTEST') == "True":
        logging.basicConfig(filename='test_app.log', format='%(asctime)s - %(message)s')
    else:
        logging.basicConfig(filename='app.log', format='%(asctime)s - %(message)s')

    @classmethod
    def log_warning_error(cls, callingMethod, message="error message not passed", *vars):
        """logs an error to the log file."""
        cleanCallingMethod = cls.clean_string(callingMethod)
        logging.critical(cls.generate_alert_message(cleanCallingMethod, message, vars))
        if os.getenv('RUN_UNITTEST') != "True":
            cls.verify_slack_message_sent(SlackChannelHandler.
                                            send_message_to_error_slack(cls.
                                                generate_alert_message(cleanCallingMethod,
                                                                       message,
                                                                       vars)))

    @classmethod
    def generate_alert_message(cls, callingMethod, message, *vars):
        """generates the error messaged that gets logged"""
        varsAsAString = "\n\t".join(map(str, vars))
        return(f"method: {callingMethod} raised error: {message}:\n\t{varsAsAString}")

    @classmethod
    def verify_slack_message_sent(cls, SlackReturn):
        """verifies slack sent correctly or logs an error to describe issue."""
        if SlackReturn == -1:
            logging.warning(cls.generate_alert_message("SystemLogging.log_warning_error()",
                                                        "Slack webhook enviromental Variable not set"))
        elif SlackReturn != 200:
            logging.warning(cls.generate_alert_message("SystemLogging.log_warning_error()",
                                                        "Unknown Issue with Slack Webhook and API. Returned error code: " + str(SlackReturn)))

    @classmethod
    def clean_string(cls, stringToClean):
        """removes whitespace and newlines from a string"""
        return (stringToClean.translate( { ord(c) :None for c in string.whitespace } ))