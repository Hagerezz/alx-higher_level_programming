#!/usr/bin/python3
""" This function"""
import urllib.request

url = "https://alx-intranet.hbtn.io/status"

try:
    with urllib.request.urlopen(url) as response:
        html_content = response.read().decode('utf-8')

        print("Body response:")
        print("\t- type:", type(html_content))
        print("\t- content:", html_content)
except urllib.error.HTTPError as e:
    print("Error code:", e.code)
except urllib.error.URLError as e:
    print("URLError:", e.reason)
