import logging
import inspect
from models.slack_handler import SlackChannelHandler

class SystemLogging:
    """handles the system logging"""
    logging.basicConfig(filename='app.log', format='%(asctime)s - %(message)s')

    @classmethod
    def log_warning_error(cls, callingMethod, message="error message not passed", *vars):
        """logs an error to the log file."""
        logging.warning(cls.generate_alert_message(callingMethod, message, vars))
        SlackChannelHandler.send_message_to_error_slack(cls.generate_alert_message(callingMethod, message, vars))

    @classmethod
    def generate_alert_message(cls, callingMethod, message, *vars):
        """generates the error messaged that gets logged"""
        varsAsAString = "\n\t".join(map(str, vars))
        return(f"{callingMethod[:-1]} raised error: {message}:\n\t{varsAsAString}")
    