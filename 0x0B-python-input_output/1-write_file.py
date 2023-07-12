#!/usr/bin/python3
"""represent a file"""


def write_file(filename="", text=""):
    """write"""
    with open(filename, 'w', encoding='utf-8') as file:
        count = file.write(text)
    return count
