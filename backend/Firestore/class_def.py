from typing import List
from datetime import datetime
from google.cloud import firestore

# class requires 2 methods: from_dict/to_dict
# defines a student
class User:
    """User represents a user in the forum with its associated attributes. methods provided are for interfacing with cloud firebase"""
    def __repr__(self) -> str:
        return "User(email = {}, firstName = {}, lastName = {}, matric = {}, password = {}, registeredCourses = {})".format(self.email, self.firstName, self.lastName, self.matric, self.password, self.registeredCourses)

    def __init__(self, email: str, firstName: str, lastName: str, matric: str, password: str, registeredCourses: List[str]) :
        self.email = email
        self.firstName = firstName
        self.lastName = lastName
        self.matric = matric
        self.password = hash(password)
        self.registeredCourses = registeredCourses

    @staticmethod
    def from_dict(**source):
        return User(**source)

    def to_dict(self):
        dest = { 
            "email" : self.email,
            "firstName": self.firstName,
            "lastName" : self.lastName,
            "matric" : self.matric,
            "password":self.password,
            "registeredCourses":self.registeredCourses
        }
        return dest 


# defines a course
class Course:
    def __repr__(self) -> str:
        return "Course(courseCoord = {}, courseMaterials = {}, courseName = {}, numUsers {})".format(self.courseCoord, self.courseMaterials, self.courseName, self.numUsers)

    def __init__(self, courseCoord: str, courseMaterials: str, courseName: str, numUsers: int):
        self.courseCoord = courseCoord
        self.courseMaterials = courseMaterials
        self.courseName = courseName
        self.numUsers = numUsers

    @staticmethod
    def from_dict(**source):
        return Course(**source)

    def to_dict(self) -> dict:
        dest = {
            "courseCoord": self.courseCoord,
            "courseMaterials": self.courseMaterials,
            "courseName": self.courseName,
            "numUsers": self.numUsers
        }
        return dest 

# defines a thread
class Thread:
    def __repr__(self) -> str:
        return "Thread(body = {}, timeStamp = {}, title = {}, userID = {}, votes = {}, views = {})".format(self.body, self.timeStamp, self.title, self.userID, self.votes, self.views)

    def __init__(self, body: str, timeStamp: datetime, title: str, userID: str, votes: int, views: int):
        self.body = body
        self.timeStamp = timeStamp
        self.title = title
        self.userID = userID
        self.votes = votes
        self.views = views 

    @staticmethod
    def from_dict(**source):
        return Thread(**source)   
    
    def to_dict(self):
        dest = { 
            "body":self.body,
            "timeStamp":self.timeStamp,
            "title":self.title,
            "userID":self.userID,
            "votes":self.votes,
            "views":self.views 
        }
        return dest


# defines a rating
class Rating: 
    def __repr__(self) -> str:
        return 
    
    def __init__(self, description, timeStamp, likes, rating): # no type descriptors 
        self.description = description,
        self.timeStamp = timeStamp,
        self.likes = likes,
        self.rating = rating
    
    @staticmethod
    def from_dict(**source):
        return Rating(**source)   
    
    def to_dict(self):
        dest = { 
            "description":self.description,
            "timeStamp":self.timeStamp,
            "likes":self.likes,
            "rating":self.rating
        }
        return dest


class Replies:
    def __repr__(self):
        return 
    
    def __init__(self, body, timeStamp, userID):
        self.body = body
        self.timeStamp = timeStamp
        self.userID = userID
    
    @staticmethod
    def from_dict(**source):
        return Rating(**source)   
    
    def to_dict(self):
        dest = { 
            "body":self.body,
            "timeStamp":self.timeStamp,
            "userID":self.userID
        }
        return dest
