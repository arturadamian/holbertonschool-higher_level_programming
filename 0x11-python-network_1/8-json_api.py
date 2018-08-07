#!/usr/bin/python3
"""
takes in a letter and sends a POST request
with the letter as a parameter
"""
import requests
from sys import argv


if __name__ == "__main__":

    if len(argv) == 2:
        letter = argv[1]
    else:
        letter = ""

    url = "http://0.0.0.0:5000/search_user"
    data = {'q': letter}
    r = requests.post(url, data)
    try:
        r_json = r.json()
        if len(r_json) == 0:
            print("No result")
        else:
            print("[{}] {}".format(r_json['id'], r_json['name']))
    except:
        print("Not a valid JSON")
