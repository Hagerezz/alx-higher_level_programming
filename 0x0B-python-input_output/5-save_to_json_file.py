#!/usr/bin/python3
"""represent a file"""
import json


def save_to_json_file(my_obj, filename):
    """save"""
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
