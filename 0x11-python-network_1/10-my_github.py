#!/usr/bin/python3
"""takes github credentials and displays id using github api"""
import requests
from sys import argv

if __name__ == "__main__":
    header = {'Authorization': "Bearer {}".format(argv[2])}
    req = requests.get("https://api.github.com/users/{}".format(argv[1]),
                        headers=header)
    try:
        print(req.json()['id'])
    except Exception:
        print(None)
