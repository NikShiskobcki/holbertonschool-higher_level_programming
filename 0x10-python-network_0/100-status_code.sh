#!/bin/bash
# sends request to URL passed as an argument
curl -s -o /dev/null -w "%{http_code}" $1
