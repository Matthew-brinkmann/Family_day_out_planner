#!/usr/bin/python3
"""module for database"""
from api.views import auth_views
from flask import render_template, request
from models.authorization_handler import AuthorizationHandler
from flask_login import login_required


# @swag_from("documentation/auth.yml", methods=['POST'])
@auth_views.route('/login', methods=['GET'], strict_slashes=False)
def login_get():
    """ login """
    return render_template("login.html")


@auth_views.route('/login', methods=['POST'], strict_slashes=False)
def login_post():
    """ login """
    return (AuthorizationHandler.user_login(request))

@auth_views.route('/signup', methods=['GET'], strict_slashes=False)
def signup_get():
    """signup page"""
    return render_template('signup.html')

@auth_views.route('/signup', methods=['POST'], strict_slashes=False)
def signup_post():
    """ validate the input and signup """
    return AuthorizationHandler.user_signup(request)

@auth_views.route('/logout', methods=['GET'], strict_slashes=False)
@login_required
def logout():
    """ logout """
    return AuthorizationHandler.user_logout(request)

if __name__ == "__main__":
    pass