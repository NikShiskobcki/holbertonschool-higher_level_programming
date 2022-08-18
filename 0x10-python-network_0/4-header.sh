#!/bin/bash
#takes URL as arg, sends a GET request to URL and displays the body of response
curl -s -X GET $1 -H "X-HolbertonSchool-User-Id: 98"
