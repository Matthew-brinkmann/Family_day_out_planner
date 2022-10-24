import logging
import os
import string
from models.slack_handler import SlackChannelHandler


class SystemLogging:
    """handles the system logging"""
    @classmethod
    def log_warning_error(cls, callingMethod, message="error message not passed", *vars):
        """logs an error to the log file."""
        cls.setup_log_config()
        cleanMethodName = cls.clean_calling_method(callingMethod)
        logging.critical(cls.generate_alert_message(cleanMethodName, message, vars))
        if os.getenv('RUN_UNITTEST', False) is False:
            cls.verify_slack_message_sent(SlackChannelHandler.
                                            send_message_to_error_slack(cls.
                                                generate_alert_message(cleanMethodName,
                                                                       message,
                                                                       vars)))

    @classmethod
    def print_to_logfile_for_debug(cls, message="message Passed", *vars):
        """prints a line to the log files for debug purposes."""
        cls.setup_log_config()
        logging.warning(cls.generate_alert_message("DEBUG_CODE", message, vars))

    @classmethod
    def setup_log_config(cls):
        """sets up the logging information."""
        if os.getenv('RUN_UNITTEST', False) is False:
            logging.basicConfig(filename='app.log', format='%(asctime)s - %(message)s')
        else:
            logging.basicConfig(filename='test_app.log', format='%(asctime)s - %(message)s')

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
    def clean_calling_method(cls, stringToClean) -> string:
        """removes whitespace and newlines from a string"""
        return (stringToClean.translate( { ord(c) :None for c in string.whitespace } ))