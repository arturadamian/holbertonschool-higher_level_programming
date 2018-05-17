#!/usr/bin/python3


class Student:
    """class student
    """
    def __init__(self, first_name, last_name, age):
        """instantation

        Args:
        first_name (str): name
        last_name (str): last name
        age (int): age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attr=None):
        """retrieves a dictionary representation of a Student

        Args:
            attr: attribures
        """
        if attr is None:
            return self.__dict__
        return {key: value
                for key, value in self.__dict__.items() if key in attr}

    def reload_from_json(self, json):
        """replaces all attributes

        Args:
            json: a dictionary
        """
        if json is None:
            return
        self.__dict__ = json
