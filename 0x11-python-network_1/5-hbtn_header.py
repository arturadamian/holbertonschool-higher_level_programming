#!/usr/bin/python3
"""
use the package requests to fetch url
"""


import requests
import sys


r = requests.get(sys.argv[1])
print(r.headers['X-Request-Id'])
