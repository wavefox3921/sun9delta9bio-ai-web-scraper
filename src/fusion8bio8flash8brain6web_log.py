# Development Log
# Started at 2025-04-03 08:35:19

# Refactored the code
# This is a random comment
# Fixed some bugs


import json

def save_to_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def load_from_json(filename):
    with open(filename, 'r') as f:
        return json.load(f)

# Update at 2025-04-04 03:45:04
# Added documentation

def reverse_string(s):
    return s[::-1]

def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]