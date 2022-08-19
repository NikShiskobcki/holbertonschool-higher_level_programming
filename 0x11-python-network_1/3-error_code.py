#!/usr/bin/python3
"""takes url, sends a request and displays body of response""" 
import sys
from urllib import request, error

if __name__ == "__main__":
    req = request.Request(sys.argv[1])
    try:
        with request.urlopen(req) as response:
            page = response.read()
    except error.HTTPError as err:
        print("Error code: " + str(err.code))
    else:
        print(page.decode("utf-8"))
