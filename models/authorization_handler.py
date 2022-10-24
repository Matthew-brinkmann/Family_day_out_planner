from models.system_logging import SystemLogging
from models.user_interface import UserInterface
from models.token import TokenHelper
from flask import jsonify, redirect, url_for
from flask_login import logout_user

class AuthorizationHandler:
    """
    handles permissions and authorises users.
    """
    @staticmethod
    def user_login(userRequestInformation):
        """
        handles getting user information from DB for login
        """
        username = userRequestInformation.form.get("username")
        password = userRequestInformation.form.get("password")
        # remember = True if userRequestInformation.form.get('remember') else False
        if UserInterface.verify_user_information(username, password) is False:
            return jsonify({"message": "Please check your login details and try again."})
        return (AuthorizationHandler.generate_json_response(
                    TokenHelper.generate_auth_token_from_user_id(
                        UserInterface.retrieve_user_id_from_username(username))))

    @staticmethod
    def user_signup(userRequestInformation):
        """
        handles adding new user to DB
        """
        username = userRequestInformation.form.get('username')
        password = userRequestInformation.form.get('password')
        if UserInterface.retrieve_user_instance_from_username(username) is not None:
            return jsonify({"message": "Username already exists, pls choose a different username."})
        new_user = UserInterface.create_new_user(username, password)
        
        return (AuthorizationHandler.generate_json_response(TokenHelper.generate_auth_token_from_user_id(new_user.id)))
        
    @staticmethod
    def user_logout(userRequestInformation):
        """
        handles logging out of user from console.
        """
        logout_user()
        return redirect(url_for('index.html'))

    @staticmethod
    def add_to_user_search_history(apiRequest):
        """verify token"""
        auth_token = apiRequest.headers.get('Authorization')
        if auth_token:
            UserInterface.add_search_history_to_user_by_id(TokenHelper.get_user_id_from_auth_token(auth_token),
                                                           apiRequest.get_json())
        return

    @staticmethod
    def generate_json_response(auth_token):
        """will explain later"""
        return jsonify({
            "message": "Operation Success!",
            "token": auth_token.decode()
        })
