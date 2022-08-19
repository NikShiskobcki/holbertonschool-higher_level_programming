#!/usr/bin/python3
"""takes a url and email and sends a post request"""
import sys
from urllib import request, parse

if __name__ == "__main__":
    dta = parse.urlencode({'email': sys.argv[2]}).encode()
    req = request.Request(sys.argv[1], dta=dta)
    with request.urlopen(req) as response:
        page = response.read()
    print(page.decode("utf-8"))
