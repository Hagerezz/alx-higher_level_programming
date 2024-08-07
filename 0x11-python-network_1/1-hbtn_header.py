#!/usr/bin/python3
"""takes in a URL, sends a request to the URL"""
if __name__ == "__main__":
    import sys
    import urllib.request
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.headers["X-Request-Id"])
