#!/usr/bin/python3
"""
Module of table Users
"""
from api.app import db
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    registered_on = db.Column(db.DateTime, nullable=False)
    search_histories = relationship("UserSearchHistory", cascade="all, delete", backref="user")

