#!/usr/bin/python3
"""
sends a POST request to the passed URL with the email
"""
import requests
import sys


if __name__ == "__main__":
    mail = {'email': sys.argv[2]}
    r = requests.post(sys.argv[1], mail)
    print(r.text)
