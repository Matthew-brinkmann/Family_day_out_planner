import os
import requests
from models.exceptions import *


class SlackChannelHandler():
    """handles the sending of a message to the slack warnings channel"""
    webhookURL = os.getenv('SLACK_WEBHOOK', None)

    @classmethod
    def send_message_to_error_slack(cls, message):
        """sends message to slack channel"""
        if cls.webhookURL is None:
            return (-1)
        bodyOfRequest = {'text': str(message)}
        return(requests.post(cls.webhookURL, json = bodyOfRequest).status_code)
