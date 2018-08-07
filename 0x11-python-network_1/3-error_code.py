#!/usr/bin/python3
"""
manages urllib.error.HTTPError exceptions and print:
Error code: followed by the HTTP status code
"""
import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as r:
            print(r.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
