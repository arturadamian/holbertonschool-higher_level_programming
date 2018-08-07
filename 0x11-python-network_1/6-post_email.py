#!/usr/bin/python3
"""
displays the value of the variable X-Request-Id
in the response header
"""
import requests
import sys


if __name__ == "__main__":
    mail = {'email': sys.argv[2]}
    r = requests.post(sys.argv[1], mail)
    print(r.text)
