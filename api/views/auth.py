#!/usr/bin/python3
"""module for database"""
from api.views import auth_views
from flask import Flask, Blueprint, render_template, jsonify, request, redirect, url_for
from models.token import TokenHelper
from models.user_interface import UserInterface
from models.db_models.users import User
from werkzeug.security import generate_password_hash, check_password_hash
from api.app import db
from flask_login import login_user, login_required, logout_user
import datetime


# @swag_from("documentation/auth.yml", methods=['POST'])
@auth_views.route('/login', methods=['GET'], strict_slashes=False)
def login_get():
    """ login """
    return render_template("login.html")


@auth_views.route('/login', methods=['POST'], strict_slashes=False)
def login_post():
    """ login """
    username = request.form.get("username")
    password = request.form.get("password")
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(username=username).first()
    if user:
        auth_token = TokenHelper.encode_auth_token(user.id)
    if not user or not check_password_hash(user.password, password) or not auth_token:
        return jsonify({"message": "Please check your login details and try again."})
    return jsonify({
        "message": "login successfully!",
        "token": auth_token.decode()
    })

@auth_views.route('/signup', methods=['GET'], strict_slashes=False)
def signup_get():
    """signup page"""
    return render_template('signup.html')

@auth_views.route('/signup', methods=['POST'], strict_slashes=False)
def signup_post():
    """ validate the input and signup """
    username = request.form.get('username')
    password = request.form.get('password')
    registered_on = datetime.datetime.now()
    user = User.query.filter_by(username=username).first()
    if user:
        return jsonify({"message": "Username already exists, pls choose a different username."})
    new_user = User(username=username, password=generate_password_hash(password, method='sha256'), registered_on=registered_on)

    db.session.add(new_user)
    db.session.commit()
    auth_token = TokenHelper.encode_auth_token(new_user.id)
    return jsonify({
        "message": "sign up successfully!",
        "token": auth_token.decode()
    })

@auth_views.route('/logout', methods=['GET'], strict_slashes=False)
@login_required
def logout():
    """ logout """
    logout_user()
    return redirect(url_for('index.html'))

if __name__ == "__main__":
    pass