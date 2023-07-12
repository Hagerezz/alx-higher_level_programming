#!/usr/bin/python3
"""represent a file"""
import sys
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

filename = 'add_item.json'
try:
    my_list = load_from_json_file(filename)
except:
    my_list = []
for arg in sys.argv[1:]:
    my_list.append(arg)
save_to_json_file(my_list, filename)
