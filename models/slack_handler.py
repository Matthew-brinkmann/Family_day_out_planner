import os
import requests


class SlackChannelHandler():
    """handles the sending of a message to the slack warnings channel"""
    webhookURL = os.getenv('SLACK_WEBHOOK')

    @classmethod
    def send_message_to_error_slack(cls, message):
        """sends message to slack channel"""
        bodyOfRequest = {'text': str(message)}
        requests.post(cls.webhookURL, json = bodyOfRequest)