#!/usr/bin/python3
"""fetches URL with urllib"""
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as responce:
        html = responce.read()
        code = html.decode('utf-8')
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- cotent: {}".format(html))
        print("\t- utf8 content: {}".format(code))
