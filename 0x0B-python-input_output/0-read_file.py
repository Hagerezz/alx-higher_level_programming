#!/usr/bin/python3
"""represent a file"""


def read_file(filename=""):
    """read"""
    with open(filename, 'r', encoding='UTF8') as file:
        r = file.read()
        print(r)
