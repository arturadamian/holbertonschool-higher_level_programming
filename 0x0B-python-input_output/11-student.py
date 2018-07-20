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

    def to_json(self):
        """retrieves a dictionary representation of a Student"""
        return self.__dict__
