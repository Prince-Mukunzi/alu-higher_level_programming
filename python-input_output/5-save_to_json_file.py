#!/usr/bin/python3
''' function that writes an Object to a text file, using a JSON representation
'''
import json


def save_to_json_file(my_obj, filename):
    '''Module save_to_json_fil
    accepts Python object and sends JSON representation to a file
    '''
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
