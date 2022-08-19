#!/usr/bin/python3
""" script that fetches https://intranet.hbtn.io/status """
import urllib.request

req = urllib.request.Request('https://intranet.hbtn.io/status')
with urllib.request.urlopen(req) as response:
    page = response(read)
tpe = type(page)
utf = page.decode('utf-8')
print("Body response:")
print("\t- type: {}".format(tpe))
print("\t- content: {}".format(page))
print("\t- utf8 content: {}".format(utf))
