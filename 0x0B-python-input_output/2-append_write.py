#!/usr/bin/python3
"""represent a file"""


def append_write(filename="", text=""):
    """append"""
    with open(filename, 'a', encoding='utf-8') as file:
        count = file.write(text)
    return count
