#!/usr/bin/python3
"""takes a url and email and sends a post request"""
from sys import argv
from urllib import request, parse

if __name__ == "__main__":
    dta = parse.urlencode({'email': argv[2]}).encode()
    req = request.Request(argv[1], dta=dta)
    with request.urlopen(req) as response:
        page = response.read()
    print(page.decode("utf-8"))
