#!/usr/bin/python3
"""script that fetches https://intranet.hbtn.io/status"""
import requests

req = requests.get('https://intranet.hbtn.io/status')
print("Body response:")
print("\t- type: {}".format(type(req.text)))
print("\t- content: {}".format(req.text))
