#!/usr/bin/python3
"""
Module of table Users search history
"""
from api.app import db
from models.users import *
from sqlalchemy import Column, String, ForeignKey


class UserSearchHistory(db.Model):
    __tablename__ = "searchHistory"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(100), ForeignKey('users.id'), nullable=False)
    search_history = db.Column(db.JSON)

