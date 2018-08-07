#!/usr/bin/python3
"""
takes in a letter and sends a POST request
with the letter as a parameter
"""
import requests
from sys import argv


if __name__ == "__main__":

    url = "https://swapi.co/api/people/?search=" + argv[1]
    r = requests.get(url)
    r_json = r.json()
    print("Number of results: {}".format(r_json['count']))
    for item in r_json['results']:
        print(item['name'])
