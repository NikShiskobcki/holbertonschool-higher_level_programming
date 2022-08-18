#!/bin/bash
# display body size of response
curl -s $1 | wc -c
