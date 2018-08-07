#!/usr/bin/python3
"""
displays the value of the variable X-Request-Id
in the response header
"""


import requests
import sys


r = requests.get(sys.argv[1])
print(r.headers['X-Request-Id'])
