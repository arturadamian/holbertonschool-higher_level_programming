#!/usr/bin/python3
"""
print Error code if the HTTP status >= 400
"""
import requests
import sys


try:
    r = requests.get(sys.argv[1])
    if r.status_code >= 400:
        print("Error code: {}".format(e))
    else:
        print(r.text)
