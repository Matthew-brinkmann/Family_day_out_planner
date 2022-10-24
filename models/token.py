import jwt
import datetime
from api.app import app
from models.db_models.users import User
from models.db_models.users_search_history import UserSearchHistory

from models.system_logging import SystemLogging


class TokenHelper:
    @staticmethod
    def generate_auth_token_from_user_id(user_id):
        """
        Generates the Auth Token
        :return: string
        """
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
                'iat': datetime.datetime.utcnow(),
                'usr_id': user_id
            }
            return jwt.encode(
                payload,
                app.config.get('SECRET_KEY'),
                algorithm='HS256'
            )
        except Exception:
            return False

    @staticmethod
    def get_user_id_from_auth_token(auth_token):
        """
        Validates the auth token
        :param auth_token:
        :return: integer|string
        """
        try:
            payload = jwt.decode(auth_token, app.config.get('SECRET_KEY'))
            return payload['usr_id']
        except jwt.ExpiredSignatureError:
            return 'Session expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'

    # TODO: add in refresh token methods to keep sessions alive.