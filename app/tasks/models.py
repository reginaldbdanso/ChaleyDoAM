#!/usr/bin/python3
"""Base model for the project"""
import uuid
from datetime import datetime


class Task:
    """Task class"""

    def __init__(self, title: str, description: str, due_date, due_date_date) -> None:
        """Initializes an instance of the Task class"""
        self.__id = uuid.uuid4()
        self.title = title
        self.description = description
        self.due_date = due_date
        self.due_date_date = due_date_date
        self.__created_at = datetime.now()
        self.__updated_at = datetime.now()
    
    @property
    def id(self):
        """Returns the id of the task"""
        return self.__id

    @property
    def created_at(self):
        """Returns the title of the task"""
        return self.__created_at

    @property
    def updated_at(self):
        """Returns the title of the task"""
        return self.__updated_at

    def to_dict(self):
        """Returns a dictionary representation of the task"""
        return {
            'id': str(self.id),
            'title': self.title,
            'description': self.description,
            'due_date': self.due_date,
            'due_date_date': self.due_date_date,
            'created_at': self.__created_at.strftime('%Y-%m-%dT%H:%M:%S.%f'),
            'updated_at': self.__updated_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        }
    
    @created_at.setter
    def created_at(self, value):
        """Sets the created_at attribute to the current datetime"""
        self.__created_at = value

    @updated_at.setter
    def updated_at(self, value):
        """Sets the updated_at attribute to the current datetime"""
        self.__updated_at = value

