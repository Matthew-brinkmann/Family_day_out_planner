import jwt
import datetime
from api.app import app
from models.users import User
from models.users_search_history import UserSearchHistory


class TokenHelper:
    @staticmethod
    def encode_auth_token(user_id):
        """
        Generates the Auth Token
        :return: string
        """
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=5),
                'iat': datetime.datetime.utcnow(),
                'sub': user_id
            }
            print(f"app.config.get('SECRET_KEY'): {app.config.get('SECRET_KEY')}")
            return jwt.encode(
                payload,
                app.config.get('SECRET_KEY'),
                algorithm='HS256'
            )
        except Exception as e:
            return e

    @staticmethod
    def decode_auth_token(auth_token):
        """
        Validates the auth token
        :param auth_token:
        :return: integer|string
        """
        try:
            payload = jwt.decode(auth_token, app.config.get('SECRET_KEY'))
            return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'


def verify_token(request):
    """verify token"""
    auth_header = request.headers.get('Authorization')
    auth_token = None
    if auth_header:
        try:
            auth_token = auth_header.split(" ")[1]
        except IndexError:
            return
    if auth_token:
        userId = TokenHelper.decode_auth_token(auth_token)
        if check_userId_exist(userId):
            searchHistory = UserSearchHistory(user_id=userId,
                                              search_history=request.get_json())
            db.session.add(searchHistory)
            db.session.commit()
    return


def check_userId_exist(userId):
    """check if userId from token exists or not"""
    if User.query.filter_by(id=userId).first():
        return True
    return False
