#!/usr/bin/python3
"""takes in a URL, sends a request to the URL"""
if __name__ == '__main__':
    from requests import get
    from sys import argv
    res = get(argv[1])
    print(res.headers.get('X-Request-Id'))
