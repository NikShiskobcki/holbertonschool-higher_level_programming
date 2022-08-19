#!/usr/bin/python3
"""takes url and email, sends post request and displays response"""
from sys import argv
import requests

if __name__ == "__main__":
    req = requests.post(argv[1], data={'email': argv[2]})
    print(req.text)
