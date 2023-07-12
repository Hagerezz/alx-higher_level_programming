#!/usr/bin/python3
"""represent a file"""


def read_file(filename=""):
    """read"""


    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read())
