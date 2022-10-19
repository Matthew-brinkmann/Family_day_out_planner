import json

from models.slack_handler import SlackChannelHandler
from unittest import TestCase
from unittest.mock import patch
import os


class TestAnalytics(TestCase):

    @patch('requests.post')
    def test_post(self, mock_post):
        info = {'text': 'test Message'}
        SlackChannelHandler.send_message_to_error_slack('test Message')
        mock_post.assert_called_with(os.getenv('SLACK_WEBHOOK'), json=info)

