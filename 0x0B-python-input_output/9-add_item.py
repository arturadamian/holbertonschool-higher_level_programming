#!/usr/bin/python3
""" adds all arguments to a Python list"""
from sys import argv

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

listik = argv[1:]
try:
    obj = load_from_json_file("add_item.json")
    save_to_json_file(obj + listik, "add_item.json")
except:

    save_to_json_file(listik, "add_item.json")
