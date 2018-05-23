#!/usr/bin/python3
"""creating Base class"""
import json
"""importing json module"""


class Base:
    """class base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """that returns the JSON string representation of list_dictionaries"""
        if not list_dictionaries and all(not d for d in list_dictionaries):
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""

        filename = cls.__name__ + ".json"
        lists_obj = []
        if list_objs:
            for lists in list_objs:
                lists_obj.append(cls.to_dictionary(lists))
        with open(filename, "w") as f:
            f.write(Base.to_json_string(lists_obj))

    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""

        if cls.__name__ == "Rectangle":
            dummy = cls(10, 19)
        if cls.__name__ == "Square":
            dummy = cls(17)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""

        filename = cls.__name__ + ".json"
        nlist = []

        try:
            with open(filename, "r") as f:
                js = f.read()
                lists = cls.from_json_string(js)
                for ls in lists:
                    nlist.append(cls.create(**ls))
        except:
            pass
        return nlist
