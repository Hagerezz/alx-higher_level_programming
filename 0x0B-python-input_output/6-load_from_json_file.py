#!/usr/bin/python3
"""represent a file"""
import json


def load_from_json_file(filename):
    """load"""
    with open(filename, 'r') as file:
        my_obj = json.load(file)
    return my_obj
