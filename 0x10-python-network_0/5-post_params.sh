#!/bin/bash
# takes in URL, sends POST request and displays body of response
curl $1 -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
