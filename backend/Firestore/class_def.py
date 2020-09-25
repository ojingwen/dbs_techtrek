from typing import List
from datetime import datetime
from google.cloud import firestore

# class requires 2 methods: from_dict/to_dict
# defines a user
class User:
    """User represents a user in the forum with its associated attributes. methods provided are for interfacing with cloud firebase"""
    def __repr__(self) -> str:
        return "User(username = {}, password = {})".format(self.username, self.password)

    def __init__(self, username: str, password: str):
        # only need username/password
        self.username = username
        self.password = password

    @staticmethod
    def from_dict(**source):
        return User(**source)

    def to_dict(self):
        dest = { 
            "username" : self.username,
            "password":self.password,
        }
        return dest 

