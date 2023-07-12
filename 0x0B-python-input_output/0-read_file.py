#!/usr/bin/python3
"""represent a file"""


def read_file(filename=""):
    """read"""

    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
