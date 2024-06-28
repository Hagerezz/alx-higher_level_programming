#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status"""
import urllib.request

if __name__ == "__main__":
    req = urllib.request.Request("https://alx-intranet.hbtn.io/status")
    with urllib.request.urlopen(req) as response:
        bod = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(bod)))
        print("\t- content: {}".format(bod))
        print("\t- utf8 content: {}".format(bod.decode("utf-8")))
