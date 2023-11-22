#!/usr/bin/python3
"""Base model for the project"""
import uuid
from datetime import datetime


class Task:
    """Task class"""

    def __init__(self, title: str, description: str, due_date, due_date_date) -> None:
        self.__id = uuid.uuid4()
        self.title = title
        self.description = description
        self.due_date = due_date
        self.due_date_date = due_date_date
        self.__created_at = datetime.now()
    


