from models.db_models.users import User
from models.db_models.users_search_history import UserSearchHistory
from models.token import TokenHelper
import datetime

class UserInterface:
    """
    is the interface for all user DB enquiries.
    """
    @staticmethod
    def user_login(userInformation):
        """
        handles getting user information from DB for login
        """
        pass

    @staticmethod
    def user_signup(userInformation):
        """
        handles adding new user to DB
        """
        pass