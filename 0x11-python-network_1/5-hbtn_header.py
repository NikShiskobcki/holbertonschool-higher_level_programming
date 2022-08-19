#!/usr/bin/python3
"""takes in URL, sends request to URL and displays value of X-Request-Id"""
import requests
import sys

if __name__ == "__main__":
    req = requests.get(sys.argv[1])
    try:
        print(req.headers['X-Request-Id'])
    except KeyError:
        pass
