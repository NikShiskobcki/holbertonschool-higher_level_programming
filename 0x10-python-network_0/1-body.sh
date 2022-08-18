#!/bin/bash
# takes in an URL, sends a GET request and displays body of response
curl -s -L -X GET $1
