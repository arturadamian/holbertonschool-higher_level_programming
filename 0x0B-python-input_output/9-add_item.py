#!/usr/bin/python3
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

from sys import argv
ls = argv[1:]
obj = load_from_json_file("add_item.json")
obj.extend(ls)
save_to_json_file(obj, "add_item.json")
