from api.app import db
import datetime
from models.db_models.users import User
from models.db_models.users_search_history import UserSearchHistory
from werkzeug.security import generate_password_hash, check_password_hash

from models.system_logging import SystemLogging


class UserInterface:
    """
    is the interface for all user DB enquiries.
    """
    @staticmethod
    def retrieve_search_history_by_id(userId):
        """
        returns list of all previous serches        
        """
        # query DB, get search hisotry filterby(user_id=userID)
        # build in a check that we don't send back any expired searches.
        # 25 i search for events on 26th., I log back in on 29th, i shouldnt see 26th events.
        # if we find old searchs (for events before today), delete from DB.
        pass
    
    @staticmethod
    def add_search_history_to_user_by_id(userId, searchHistoryRequestJson):
        """
        add new search history to DB        
        """
        if UserInterface.retrieve_user_instance_from_userid(userId) is None:
            return False
        searchHistory = UserSearchHistory(user_id = userId,
                                          search_history = searchHistoryRequestJson)
        db.session.add(searchHistory)
        db.session.commit()

    @staticmethod
    def create_new_user(username, password):
        """
        adds a new user to the DB
        """
        newUser = User(username=username,
                       password=generate_password_hash(password, method='sha256'),
                       registered_on=datetime.datetime.now())
        db.session.add(newUser)
        db.session.commit()
        return (newUser)

    @staticmethod
    def verify_user_information(username, password):
        """
        verifies username and password
        """
        userInstance = UserInterface.retrieve_user_instance_from_username(username)
        if userInstance is None:
            return False
        if not check_password_hash(userInstance.password, password):
            return False
        return True

    @staticmethod
    def retrieve_user_instance_from_username(username):
        '''
        gets a user_id if exists from a username.
        '''
        return (User.query.filter_by(username=username).first())

    @staticmethod
    def retrieve_user_id_from_username(username):
        '''
        gets a user_id if exists from a username.
        '''
        userId = None
        try:
            userId = User.query.filter_by(username=username).first().id
        except AttributeError:
            return (userId)
        return (userId)

    @staticmethod
    def retrieve_user_instance_from_userid(userId):
        '''
        gets a user_id if exists from a username.
        '''
        return (User.query.filter_by(id=userId).first())
